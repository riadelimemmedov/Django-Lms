from django.shortcuts import render

#Rest
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

#Imported Models and Serializers Class
from book.models import Book
from book.serializers import BookSerializer
from custom_user.permissions import LibrarianRequired
from .models import Librarian
from .serializers import LibrarianSerializer

# Create your views here.




#!CreateBook
class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [LibrarianRequired]

#!BookDetail
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [LibrarianRequired]
    









#~Only Staff Admin => Librarian Create and Delete

#!LibrarianCreate
class LibrarianCreate(generics.CreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    # permission_classes = [IsAdminUser]

#!LibrarianDelete
class LibrarianDelete(generics.RetrieveDestroyAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    
    
    # permission_classes = [IsAdminUser]
