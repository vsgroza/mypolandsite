from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('category/<str:pk>', category_list, name='category_list'),
]