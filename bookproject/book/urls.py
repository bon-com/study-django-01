from django.urls import path
from . import views

# アプリ名
# アプリ名をつけることで、どのアプリのどの関数を呼び出しているのか把握可能
# ただし、アプリ名をつけると他のアプリ＞urlsもアプリ名を強制される
app_name = 'book'

# URLと関数をルーティングする
# 第一引数：URL
# 第二引数：関数名
# 第三引数：URL名
urlpatterns = [
    path('', views.index_view, name='index'),
    path('book/', views.list_books, name='list_books'),
    path('book/<int:pk>/detail/', views.detail_book, name='detail_book'),
    path('book/create/', views.create_book, name='create_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('book/<int:pk>/update/', views.update_book, name='update_book'),
    path('book/<int:pk>/review/', views.review_book, name='review_book')
]