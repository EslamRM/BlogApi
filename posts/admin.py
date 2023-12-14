""" To register apps in admin """
from django.contrib import admin
from .models import Post

admin.site.register(Post)
