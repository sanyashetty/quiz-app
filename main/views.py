from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Question, Set
from datetime import datetime
from django.views.generic.detail import DetailView
from django.utils import timezone


class SetDetailView(DetailView):
    model = Set
    template_name = "edit_set.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['questions'] = Question.objects.filter(set = self.get_object())
        return context

    


def main_view(request):
    # if request.method == 'POST' and request.POST['title'] != "":
    #     set = Set.objects.create(
    #         title=request.POST['title'],
    #         course=request.POST['course'],
    #         description=request.POST['description'],
    #         created_at=datetime.now()
    #     )
    #     set.save()
    sets = Set.objects.filter(author = request.user)
    return render(request, 'main.html',{'sets': sets})


def splash_view(request):
    return render(request, 'splash.html')


def login_view(request):
    # getting user info from form to log in an existing user
    username, password = request.POST['username'], request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        # if invalid user, give error message
        return redirect('/splash?error=LoginError')


def signup_view(request):
    # checking is password is at least 8 characters
    if len(request.POST['password']) < 8:
        return redirect('/splash?error=SignupError')

    # getting user info from form to sign up a new user
    user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email'],
    )
    login(request, user)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/splash')

def newset_view(request):
    if request.method == 'POST' and request.POST['body'] != "":
        set = Set.objects.create(
            title=request.POST['title'],
            course=request.POST['course'],
            description=request.POST['description'],
            created_at=datetime.now(),
            author = request.user
        )
        set.save()
    sets = Set.objects.all().order_by('-created_at')
    return render(request, 'newset.html')

def edit_set_view(request, set_id):
    if request.method == 'POST' and request.POST['body'] != "":
        question = Question.objects.create(
            body=request.POST['body'],
            answer=request.POST['answer'],
            created_at=datetime.now(),
            set = Set.objects.get(pk=set_id)
        )
        question.save()
    return redirect('/editset/'+str(set_id))