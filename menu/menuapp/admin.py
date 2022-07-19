from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Dish, Reviews
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    """Категории"""
    list_display = ('id','name', 'urls')
    list_display_links = ('name',)


class ReviewInLine(admin.TabularInline):
    """Отображение отзывов к каждому фильму"""
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Dish)
class DishAdmin(TranslationAdmin):
    """Блюда"""
    list_display = ('name', 'urls', 'get_image')
    readonly_fields = ('get_image',)
    list_display_links = ('name',)
    list_filter = ('name', 'cooking_time')
    search_fields = ('name',)
    inlines = [ReviewInLine]
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="90" height="65" ')

    get_image.short_description = 'Изображение'


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ('name', 'email', 'parent', 'dish', 'id')
    readonly_fields = ('name', 'email')


admin.site.site_title = 'Django Dishes'
admin.site.site_header = 'Django Dishes'

# AGCHERNYAVSKAYA
# Pass567
