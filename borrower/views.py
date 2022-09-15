#Django 
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

#Rest Framework
from rest_framework.views import APIView
from rest_framework import response,status

#Imported Models
from .serializers import BorrowerSerializer
from custom_user.permissions import *
from .models import BorrowedUser


# Create your views here.

#!ListBorrowerBook
class ListBorrowerBook(APIView):
    # permission_classes = [BorrowerRequired]
    def get(self,request,format=None):
        borrowed_books = BorrowedUser.objects.filter(user=self.request.user).all()
        serializer = BorrowerSerializer(borrowed_books,many=True)
        print('isledi bura birinci ')
        return response.Response(data=serializer.data,status=status.HTTP_200_OK)
    #~add permisson class after finish serializerss

#!ListBorrowedBooksLibrary
class ListBorrowedBooksLibrary(APIView):
    # permission_classes = [BorrowerRequired]
    def get(self,request,library_id,format=None):
        books = BorrowedUser.objects.filter(borrowed_library=library_id,user=self.request.user).all()
        serializer = BorrowerSerializer(books,many=True)
        print('books belong library ', books)
        return response.Response(data=serializer.data,status=status.HTTP_200_OK)
    #~add permisson class after finish serializerss
    

#!ReturnBorrowedBooks
class ReturnBorrowedBooks(ListBorrowerBook):
    def get(self,request,format=None):
        returned_books = BorrowedUser.objects.filter(user=self.request.user).delete()
        return HttpResponse('Successfully Returned Books To Library',status=status.HTTP_200_OK)
    #~add permisson class after finish serializerss
        