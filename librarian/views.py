from django.shortcuts import render

#Rest
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

#Imported Models and Serializers Class
from .models import Librarian
from .serializers import LibrarianSerializer

# Create your views here.










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
