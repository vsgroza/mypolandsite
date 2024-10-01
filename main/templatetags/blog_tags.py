from django import template
from main.models import Category

register = template.Library()


@register.simple_tag()
def get_all_categories():
    """Кнопки категорий"""
    return Category.objects.all()
