#Rest Framework
from rest_framework import serializers

#Django Models and Function
from .models import *
from book.models import Book
from book.serializers import BookSerializer
from custom_user.models import CustomUser
from library.models import *
from library.serializers import LibrarySerializer

#!BorrowerSerializers
class BorrowerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    borrowed_library = LibrarySerializer(read_only=True)
    borrowed_books = serializers.StringRelatedField(read_only=True,many=True)
    
    class Meta:
        model = BorrowedUser
        fields = ['id','user','borrowed_books','borrowed_library']
        depth=1
        
    def validate_user(self, attrs):
        custom_user = BorrowedUser.objects.filter(user=attrs)
        if attrs.role != CustomUser.BORROWER_ROLE_CODE:
            raise serializers.ValidationError('Please Select Borrower User')
        

