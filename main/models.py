from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Set(models.Model):
    title = models.TextField(max_length=300)
    course = models.TextField(max_length=300)
    description = models.TextField(max_length=600)
    #ForeignKey is for many-to-one relationship --> many sets to one user
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField()
    
    def __str__(self):
        return self.body

class Question(models.Model):
    body = models.TextField(max_length=300)
    answer = models.TextField(max_length=300)
    #ForeignKey is for many-to-one relationship --> many questions to one set
    set = models.ForeignKey(Set, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField()
    
    def __str__(self):
        return self.body
