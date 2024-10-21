from django.shortcuts import render, redirect
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForm, LoginForm, RegisterForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# def index(request):
#     """Для главной страницы"""
#     posts = Post.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'title': 'Главная страница',
#         'posts': posts,
#         'categories': categories,
#
#     }
#     return render(request, 'main/index.html', context)

class Index(ListView):
    """Для главной страницы"""
    model = Post
    context_object_name = 'posts'
    template_name = 'main/index.html'
    extra_context = {'title': 'Главная страница',}


# def category_list(request, pk):
#     """Реацкция на нажатие кнопки категории"""
#     posts = Post.objects.filter(category_id=pk)
#     categories = Category.objects.all()
#     context = {
#         'title': posts[0].category,
#         'posts': posts,
#         'categories': categories,
#     }
#     return render(request, 'main/index.html', context)

class ArticByCategory(ListView):
    """Реакция на нажатие кнопки категории"""

    def get_queryset(self):
        """Здесь можем переделать фильтрации"""
        return Post.objects.filter(category_id=self.kwargs['pk'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        """Для динамических данных"""
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context



# def post_detail(request, pk):
#     """Странички статьи"""
#     article = Post.objects.get(pk=pk)
#     Post.objects.filter(pk=pk).update(watched=F('watched') + 1)
#     ext_post = Post.objects.all().exclude(pk=pk).order_by('-watched')
#     context = {
#         'title': article,
#         'post': article,
#         'ext_post': ext_post,
#     }
#     return render(request, 'main/article_detail.html', context)

class PostDetail(DetailView):

    template_name = 'main/article_detail.html'

    def get_queryset(self):
        """Здесь дополнительная фильтрация"""
        return Post.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Для динамических данных"""
        Post.objects.filter(pk=self.kwargs['pk']).update(watched=F('watched')+1)
        context = super().get_context_data()
        post = Post.objects.get(pk=self.kwargs['pk'])
        posts = Post.objects.all().exclude(pk=self.kwargs['pk']).order_by('-watched')[:5]
        context['title'] = post.title
        context['ext_posts'] = posts
        return context

# def add_post(request):
#     """Добавление статьи от пользователя, без админки"""
#     if request.method == 'POST':
#         form = PostAddForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = Post.objects.create(**form.cleaned_data)
#             post.save()
#             return redirect('post_detail', post.pk)
#
#     else:
#         form = PostAddForm()
#
#     context = {
#         'form': form,
#         'title': 'Добавить статью'
#     }
#
#     return render(request, 'main/article_add_form.html', context)

class AddPost(CreateView):
    """Добавление статьи без админки"""
    form_class = PostAddForm
    template_name = 'main/article_add_form.html'
    extra_context = {'title': 'Добавить статью'}



class PostUpdate(UpdateView):
    """Изменение статьи"""
    model = Post
    form_class = PostAddForm
    template_name = 'main/article_add_form.html'
    extra_context = {'title': 'Изменить статью'}


class PostDelete(DeleteView):
    """Удаление статьи"""
    model = Post
    success_url = reverse_lazy('index')
    context_object_name = 'post'
    extra_context = {'title': 'Удаление статьи'}



def user_login(request):
    '''Аутентификация пользователя'''
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в аккаунт')
            return redirect('index')
    else:
        form = LoginForm()  # Здесь инициализируем форму, если запрос не POST

    context = {
        'title': 'Авторизация пользователя',
        'form': form,
    }

    return render(request, 'main/login_form.html', context)


def user_logout(request):
    '''Выход пользователя'''
    logout(request)
    return redirect('index')


def register(request):
    """Регистрация"""
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    context = {
        'title': 'Регистрация пользователя',
        'form': form,
    }

    return render(request, 'main/register.html', context)
