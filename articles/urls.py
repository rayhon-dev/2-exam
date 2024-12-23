from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('create/', views.article_add, name='create'),
    path('detail/<int:pk>/', views.article_detail, name='detail'),
    path('category/<str:category>/', views.article_by_category, name='category')
]