from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('book/', views.list_books, name='list_books'),
    path('book/<int:pk>/detail/', views.detail_book, name='detail_book'),
    path('book/create/', views.create_book, name='create_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('book/<int:pk>/update/', views.update_book, name='update_book'),
    path('book/<int:pk>/review/', views.review_book, name='review_book')
]