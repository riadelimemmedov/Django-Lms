from django.shortcuts import render,redirect,reverse,HttpResponse
from django.contrib.auth import authenticate

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
from .serializers import LibrarianSerializer,LendBookSerializer

# Create your views here.

#!CreateBook
class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [LibrarianRequired]

#!BookDetail
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [LibrarianRequired]
    

#!RegisterLibrarian => First Create CustomUser Model For Borrower User Account
class RegisterBorrower(generics.CreateAPIView):#!Book Borrower
    queryset  = CustomUser.objects.all()
    serializer_class = RegisterCustomUser
    permission_classes = [LibrarianRequired]
    
    def post(self,*args,**kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        email = self.request.POST['email']
        if(CustomUser.objects.filter(username=username).exists()):
            return response.Response('This borrower account already exists')
        else:
            newLibrarian = CustomUser(username=username)
            newLibrarian.set_password(password)
            newLibrarian.email = email
            newLibrarian.role = 'BORROWER'
            newLibrarian.save()
            return redirect('librarian:create-book-borrower')

#!BorrowerCreate
class CreateBorrowedUser(generics.CreateAPIView):
    queryset = BorrowedUser.objects.all()
    serializer_class = BorrowerSerializer  
    permission_classes = [LibrarianRequired]
    
    def post(self,*args,**kwargs):
        user = self.request.POST['user']
        if user != '':
            custom_user = CustomUser.objects.filter(id=user,role='BORROWER').first()
            if custom_user == None:
                return response.Response('Please Select Borrower User')

            borrowed_user = BorrowedUser.objects.filter(user=custom_user).exists()
            if borrowed_user:
                return redirect(reverse('librarian:lend-book-borrower'))
            else:
                BorrowedUser.objects.create(user=custom_user).save()
                return redirect(reverse('librarian:lend-book-borrower'))
            
#!LendBorrowToBorrowedUser
class LendBorrowToBorrowedUser(generics.CreateAPIView):
    queryset = BorrowedUser.objects.all()
    serializer_class = LendBookSerializer
    permission_classes = [LibrarianRequired]
    
    def perform_create(self,serializer):
        return_date = self.request.POST['return_date']
        
        user = CustomUser.objects.get(id=self.request.POST['user'])
        serializer.save(user=user)
        serializer.send_email(return_date,user.email)

#!BorrowerDelete
class BorrowerDelete(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = BorrowerSerializer
    permission_classes = [LibrarianRequired]
    