from django.shortcuts import render,redirect,reverse,HttpResponse

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
    # permission_classes = [LibrarianRequired]

#!BookDetail
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [LibrarianRequired]
    

#!RegisterLibrarian => First Create CustomUser Model For Borrower User Account
class RegisterBorrower(generics.CreateAPIView):#!Book Borrower
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
        return redirect('librarian:lend-book-borrower')

#!BorrowerCreate
class CreateBorrowedUser(generics.CreateAPIView):
    queryset = BorrowedUser.objects.all()
    serializer_class = BorrowerSerializer  
    # permission_classes = [LibrarianRequired]
    
    def post(self,*args,**kwargs):
        user = self.request.POST['user']
        if user != '':
            custom_user = CustomUser.objects.filter(id=user,role='BORROWER').first()
            if custom_user == None:
                return response.Response('Please Select Borrower User')

            borrowed_user,created = BorrowedUser.objects.get_or_create(user=custom_user)
            if borrowed_user:
                return redirect(reverse('librarian:lend-book-borrower',kwargs={'pk':borrowed_user.pk}))
            elif created:
                return HttpResponse('Borrowed user successfully created')
class LendBorrowToBorrowedUser(generics.RetrieveUpdateAPIView):
    queryset = BorrowedUser.objects.all()
    serializer_class = LendBookSerializer
    
    def put(self, request, *args, **kwargs):
        print(self.request.POST['borrowed_library'])
        is_borrowed_library = BorrowedUser.objects.filter(borrowed_library__id=self.request.POST['borrowed_library']).all().first()
        if is_borrowed_library:
            is_borrowed_library.borrowed_books.add(self.request.POST['borrowed_books'])
            is_borrowed_library.save()
        else:
            print('user ', self.request.POST['user'])
            custom_user = CustomUser.objects.get(id=self.request.POST['user'])
            borrowed_user = BorrowedUser.objects.create(user=custom_user)
            borrowed_user.save()
        # print('borrowed_library ', borrowed_library)
        print('requuest data user update ' , self.request.POST)
        print('upddate data successfully')
        return HttpResponse('update oldu ala user borrowed')
    
    #kitabxananida yoxlamalisan fuckkkkkkk evvelceden olub olmamagini

#!BorrowerDelete
class BorrowerDelete(generics.DestroyAPIView):
    queryset = BorrowedUser.objects.all()
    serializer_class = BorrowerSerializer
    # permission_classes = [LibrarianRequired]
    
    
# class LendBookToBorrowUser(generics.RetrieveUpdateAPIView):
#     queryset = BorrowedUser.objects.all()
#     serializer_class = BorrowerSerializer

#     def post(self, request, *args, **kwargs):
#         data = self.request.data
#         borrowed_books = data['borrowed_books']
#         print('borrowed_book ', )
#         borrower_user = BorrowedUser.objects.get(user=data['user'])
#         borrower_user.borrowed_books.set(borrowed_books)
#         borrower_user.save()
#         print('fuck noldu amk')
#         # borrower_user.borrowed_books.add(data[])
        
#         print('borrower_user ', borrower_user)
#         print('data value ', data)
#         return HttpResponse('put request send')
    

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
