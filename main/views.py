from unicodedata import category

from django.shortcuts import render
from .models import Category, Post



def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Главная страница',
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'main/index.html', context)

def category_list(request):
    """Реацкция на нажатие кнопки категории"""
    posts = Post.objects.filter(category_id=pk)
    categories = Category.objects.all()
    context = {
        'title': posts[0].category,
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'main/index.html', context)
