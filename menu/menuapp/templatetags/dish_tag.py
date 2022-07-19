from django import template
from menuapp.models import Category, Dish

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод категорий"""
    return Category.objects.all()


@register.inclusion_tag('menuapp/tags/last_dish.html')
def get_last_dishes(count=5):
    """Вывод последних добавленных блюд"""
    dishes = Dish.objects.order_by("id")[:count]
    return {"last_dishes": dishes}
