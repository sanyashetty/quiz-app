
from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('splash/', views.splash_view, name='splash_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('newset/', views.newset_view, name='newset_view'),
    path('editset/<int:set_id>/addqs', views.edit_set_view, name='add_question'),
    path('editset/<int:pk>/', views.SetDetailView.as_view(), name='set_detail'),
]
