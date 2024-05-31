from django.shortcuts import render, get_object_or_404

from books.models import Book, Author


def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)


def authors(request):
    Author.objects.create(name="ddaw", bio="hello world")
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author_list.html', context)

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    context = {'book': book}
    return render(request, 'book_detail.html', context)

def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    context = {'author': author}
    return render(request, 'author_detail.html', context)

def books_ordered(request):
    books = Book.objects.all().order_by('-title')
    context = {'books': books}
    return render(request, 'book_list_ordered.html', context)