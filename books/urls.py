from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('books/', views.books, name='books'),
    path('authors/', views.authors, name='authors'),
    path('books/<int:id>', views.book, name='book'),
    path('authors/<int:id>', views.author, name='author'),
]