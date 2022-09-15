from django.urls import path
from .views import *

app_name = 'borrower'
urlpatterns = [
    path('borrower-books/',ListBorrowerBook.as_view(),name='borrowed-books'),
    path('borrowed-books/library/<int:library_id>/',ListBorrowedBooksLibrary.as_view(),name='borrowed-books-library'),
    path('return-books/borrowed/',ReturnBorrowedBooks.as_view(),name='borrowed-books-library')
]
