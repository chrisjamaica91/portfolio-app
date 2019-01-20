from django.shortcuts import render
from .models import Blog


def allblogs(request):
    blogs = Blog.objects
    return render (request, 'blogs/allblogs.html', {'blogs': blogs})
