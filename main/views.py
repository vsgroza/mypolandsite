from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import Category, Post



def index(request):
    posts = Post.objects.all()
    context = {
        'title': 'Главная страница',
        'posts': posts
    }
    return render(request, 'main/index.html', context)
