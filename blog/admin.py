from django.contrib import admin

from .models import Company, Post, Category, Comment

models = [Company, Post, Category, Comment]

# Register your models here.
admin.site.register(models)
