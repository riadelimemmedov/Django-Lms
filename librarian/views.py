from django.shortcuts import render,redirect,HttpResponse

#Rest
from rest_framework import generics,response
from rest_framework.permissions import IsAdminUser


#Imported Models and Serializers Class
from book.models import Book
from book.serializers import BookSerializer
from borrower.models import BorrowedUser
from borrower.serializers import BorrowerSerializer
from custom_user.permissions import LibrarianRequired
from custom_user.models import CustomUser
from custom_user.serializers import RegisterCustomUser
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
    

#!RegisterLibrarian => First Create CustomUser Model For Borrower User Account
class RegisterBorrower(generics.ListCreateAPIView):
    queryset  = CustomUser.objects.all()
    serializer_class = RegisterCustomUser
    # permission_classes = [LibrarianRequired]
    
    def post(self,*args,**kwargs):
        print('request post data ', self.request.POST)
        print('username ', self.request.POST['username'])
        username = self.request.POST['username']
        password = self.request.POST['password']
        
        newLibrarian = CustomUser(username=username)
        newLibrarian.set_password(password)
        newLibrarian.role = 'BORROWER'
        newLibrarian.save()
        print('Creacte borrower user successfully')
        return HttpResponse('created borrower book successfully')
        #?After Created User,redirect to create/borrower/ url and create BorrowedUser Object
        # return redirect('library:librarian-create')

#!BorrowerCreate
class BorrowerCreate(generics.CreateAPIView):
    queryset = BorrowedUser.objects.all()
    serializer_class = BorrowerSerializer    
    
    def perform_create(self, serializer):
        user = self.request.POST['user']
        if user != '':
            custom_user = CustomUser.objects.get(id=user)
            serializer.save(user=custom_user)
            print('successfully created borrower user')
    
    


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
