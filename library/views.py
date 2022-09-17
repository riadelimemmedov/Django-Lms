from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth import authenticate

#Rest
from rest_framework import generics,response
from rest_framework import permissions
from custom_user.permissions import *

#Imported Models and Serializers Class
from librarian.models import Librarian
from librarian.serializers import LibrarianSerializer
from .models import Library
from custom_user.serializers import RegisterCustomUser
from custom_user.models import CustomUser
from .serializers import *

# Create your views here.

# class LibrarianList(generics.ListCreateAPIView):
#     queryset = Library.objects.all()
#     serializer_class = LibrarySerializer


###########################################################################
#Library CRUD Section
#!LibraryList
class LibraryListCreate(generics.ListCreateAPIView):#!+
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [AdminRequired]#?Or Used permissions.IsAdminUser


#!LibraryDetail
class LibraryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [AdminRequired]#?Or Used permissions.IsAdminUser
#############################################################################


###########################################################################
#Register User and Create Librarian and Delete Librarian
#!RegisterLibrarian => First Create CustomUser Model For Librarian Account
class RegisterLibrarian(generics.ListCreateAPIView):
    queryset  = CustomUser.objects.all()
    serializer_class = RegisterCustomUser
    permission_classes = [AdminRequired]#?Or Used permissions.IsAdminUser
    
    def post(self,*args,**kwargs):
        print('request post data ', self.request.POST)
        print('username ', self.request.POST['username'])
        username = self.request.POST['username']
        password = self.request.POST['password']
        
        if(authenticate(username=username,password=password)):
                return response.Response('This librarian account already exists')
        else:
            newLibrarian = CustomUser(username=username)
            newLibrarian.set_password(password)
            newLibrarian.role = 'LIBRARIAN'
            newLibrarian.save()
            #?After Created User,redirect to create/librarian/ url and create Librarian Object
            return redirect('library:librarian-create')


#!LibrarianListCreate
class LibrarianCreate(generics.CreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = [AdminRequired]#?Or Used permissions.IsAdminUser


#!LibrarianDelete
class LibrarianDelete(generics.DestroyAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = [AdminRequired]#?Or Used permissions.IsAdminUser
###########################################################################
