from django.urls import path
from .views import *
urlpatterns = [
    # path('', index, name='index'),
    path('', Index.as_view(), name='index'),
    # path('category/<str:pk>', category_list, name='category_list'),
    path('category/<int:pk>/', ArticByCategory.as_view(), name='category_list'),
    path('post/<int:pk>', post_detail, name='post_detail'),
    path('add_article/', add_post, name='add'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]