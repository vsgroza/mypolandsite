from django.db import models

class Category(models.Model):
    """Название категорий"""
    title = models.CharField(max_length=100, verbose_name='Название категории')

    """Показывает в базе название категории, а не объекта"""
    def __str__(self):
        return self.title

    """Указывает в таблицах множественное и единственное число"""
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):
    """Формируем модель статьи (Поста)"""
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(default='Скоро тут будет статья', verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата созадания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='static/css/photos', blank=True, null=True)
    author = models.CharField(max_length=255, verbose_name="Автор статьи")
    watched = models.IntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    """Показывает в базе название поста, а не объекта"""

    def __str__(self):
        return self.title

    """Указывает в таблицах множественное и единственное число"""

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'