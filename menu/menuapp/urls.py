from django.urls import path
from . import views

urlpatterns =[
    path("", views.DishesView.as_view()),
    path("dish/", views.DishListView.as_view()), #rest_framework
    path("dish/<int:pk>/", views.DishDetailsView.as_view()),#rest_framework
    path("review/", views.ReviewCreateView.as_view()),#rest_framework
    path("filter/", views.FilterDishesView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("<slug:slug>/", views.DishDetailView.as_view(),name='dish_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(),name='add_review'),

]




