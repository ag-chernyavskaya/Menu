from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    urls = models.SlugField(max_length=160, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Dish(models.Model):
    """Блюда"""
    name = models.CharField("Блюдо", max_length=150)
    description = models.TextField("Состав")
    recipe = models.TextField("Рецепт")
    image = models.ImageField("Изображение", upload_to="dishes/")
    cooking_time = models.CharField("Время приготовления", max_length=50)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    urls = models.SlugField(max_length=160, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dish_detail',kwargs={'slug': self.urls})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ['id']


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    # rest_framework
    # parent = models.ForeignKey(
    #     "self", verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    parent = models.ForeignKey(
        "self", verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
        )
    dish = models.ForeignKey(Dish, verbose_name="блюдо", on_delete=models.CASCADE)
    # rest_framework
   # dish = models.ForeignKey(Dish, verbose_name="блюдо", on_delete=models.CASCADE, related_name='reviews')
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}-{self.dish}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"







