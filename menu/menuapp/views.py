from django.db.models import Q
from django.shortcuts import redirect
from .models import Dish
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DishListSerializer, DishDetailSerializer, ReviewCreateSerializer
from rest_framework import generics, permissions


class CookingTime:
    """Время приготовления блюда"""
    def get_cooking_time(self):
        return Dish.objects.filter().values('cooking_time').distinct()


class DishesView(CookingTime, ListView): #django
    """Список блюд"""
    model = Dish
    queryset = Dish.objects.all()
    paginate_by = 9


class DishListView(generics.ListAPIView): #rest_framework
    """Вывод списка блюд"""
    serializer_class = DishListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        dishes = Dish.objects.all()
        return dishes


class DishDetailView(CookingTime, DetailView):
    """Полное описание блюда"""
    model = Dish
    slug_field = 'urls'


class DishDetailsView(generics.RetrieveAPIView): #rest_framework
    """Вывод блюда"""
    queryset = Dish.objects.filter()
    serializer_class = DishDetailSerializer


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        dish = Dish.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.dish = dish
            form.save()
        return redirect(dish.get_absolute_url())


class ReviewCreateView(generics.CreateAPIView):          #rest_framework
    """Добавление отзыва"""
    serializer_class = ReviewCreateSerializer


class FilterDishesView(CookingTime, ListView):
    """Фильтр блюд"""
    paginate_by = 3

    def get_queryset(self):
        queryset = Dish.objects.filter(cooking_time__in=self.request.GET.getlist("cooking_time"))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cooking_time'] = ''.join([f'cooking_time={x}&' for x in self.request.GET.getlist("cooking_time")])
        return context


class Search(ListView):
    """Поиск блюда"""

    paginate_by = 3
    def get_queryset(self):
        q = self.request.GET.get("q")
        dishes = Dish.objects.filter(Q(name__iregex=q))
        return dishes

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


