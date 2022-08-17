from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Quiz
admin.site.register(Post)
admin.site.register(Quiz)