from rest_framework import serializers
from .models import Dish, Reviews


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильт комметарией, только родительские"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Рекурсивный вывод дочерних комментариев"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class DishListSerializer(serializers.ModelSerializer):
    """Список блюд"""
    class Meta:
        model = Dish
        fields = ('name', 'category')


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзывов"""

    class Meta:
        model = Reviews
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзывов"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Reviews
        fields = ("name", "text", "children")


class DishDetailSerializer(serializers.ModelSerializer):
    """Полное блюдо"""
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Dish
        fields = '__all__'
        
        
