#Rest Framework
from rest_framework import serializers

#Django Models and Function
from borrower.models import BorrowedUser
from .models import *

#!LibrarianSerializer
class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'
        
class LendBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedUser
        fields = ['id','user','borrowed_books','borrowed_library']
