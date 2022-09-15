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
]
