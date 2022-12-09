from django.contrib import admin

# Register your models here.
from .models import Question,Set
admin.site.register(Question)
admin.site.register(Set)

