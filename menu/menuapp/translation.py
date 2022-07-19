from modeltranslation.translator import register, TranslationOptions
from .models import Category, Dish


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Dish)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'recipe', 'cooking_time')