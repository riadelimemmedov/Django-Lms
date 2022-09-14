from django.shortcuts import render

#Rest
from rest_framework import generics
from rest_framework import permissions

#Imported Models and Serializers Class
from .models import *
from .serializers import *

# Create your views here.

# class LibrarianList(generics.ListCreateAPIView):
#     queryset = Library.objects.all()
#     serializer_class = LibrarySerializer


###########################################################################
#~Library CRUD Section

#!LibraryList
class LibraryList(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    # permission_classes = [permissions.IsAdminUser]


#!LibraryDetail
class LibraryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    # permission_classes = [permissions.IsAdminUser]

#############################################################################
