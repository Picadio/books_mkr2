from datetime import datetime

from django.test import TestCase
from django.test import TestCase
from django.urls import reverse

from books.models import Book, Author


class BooksTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="test", bio="test")
        self.book = Book.objects.create(title="test",
                                        description="test", price=12, publication_date=datetime.now(), cover_image="test.png")

    def test_books_view(self):
        response = self.client.get(reverse("books:books"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book_list.html")

    def test_author_detail_view(self):
        response = self.client.get("/authors/author_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "author_detail.html")

    def test_authors_view(self):
        response = self.client.get(reverse("books:authors"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "author_list.html")

    def test_books_ordered_view(self):
        response = self.client.get(reverse("books:books_ordered"))
        self.assertEqual(response.status_code, 200)

    def test_book_detail_view(self):
        response = self.client.get("/books/book_detail/1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book_detail.html")