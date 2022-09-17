from django.urls import path
from .views import *

app_name = 'librarian'
urlpatterns = [
    #CRUD Book 
    path('create/book/',CreateBook.as_view(),name='create-book'),
    path('book/<int:pk>/',BookDetail.as_view(),name='book-detail'),
    
    #Create Borrower and Delete Borrower
    path('register/borrower/account/',RegisterBorrower.as_view(),name='register-borrower'),
    path('create/borrowed/user/',CreateBorrowedUser.as_view(),name='create-book-borrower'),
    path('delete/borrower/<int:pk>/',BorrowerDelete.as_view(),name='borrower-delete'),
    path('lend/book/borrower/',LendBorrowToBorrowedUser.as_view(),name='lend-book-borrower'),
    
]
