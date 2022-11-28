from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    body = models.TextField(max_length=300)
    #ForeignKey is for many-to-one relationship --> many tweets to one user
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    created_at = models.DateTimeField()
    
    def __str__(self):
        return self.body
