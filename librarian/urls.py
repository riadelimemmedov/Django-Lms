from django.urls import path
from .views import *

app_name = 'librarian'
urlpatterns = [
    #Librarian Create and Delete
    path('',LibrarianCreate.as_view(),name='librarian-create'),
    path('delete-librarian/<int:pk>/',LibrarianDelete.as_view(),name='librarian-delete'),
    
    #CRUD Book 
    path('create/book/',CreateBook.as_view(),name='create-book'),
    path('book/<int:pk>/',BookDetail.as_view(),name='book-detail'),
    
    #Create Borrower and Delete Borrower
    path('register/borrower/account/',RegisterBorrower.as_view(),name='register-borrower'),
    path('create/borrowed/user/',CreateBorrowedUser.as_view(),name='create-book-borrower'),
    path('delete/borrower/<int:pk>/',BorrowerDelete.as_view(),name='borrower-delete'),
    path('lend/book/borrower/<int:pk>/',LendBorrowToBorrowedUser.as_view(),name='lend-book-borrower'),
    # path('lend/book/borrower/<int:pk>/',LendBookToBorrowUser.as_view(),name='borrower-lend'),
    
]
