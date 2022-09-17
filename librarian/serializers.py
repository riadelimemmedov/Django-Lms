#Rest Framework
from rest_framework import serializers

#Django Models and Function
from borrower.models import BorrowedUser
from custom_user.models import CustomUser
from .models import *

#!LibrarianSerializer
class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'
        
    def validate_user(self, attrs):
        if attrs.role != CustomUser.LIBRARIAN_ROLE_CODE:
            raise serializers.ValidationError('Please Select Borrower User')


#!LendBookSerializer
class LendBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedUser
        fields = ['id','user','borrowed_books','age','borrowed_library']

    def validate_user(self, attrs):
        custom_user = BorrowedUser.objects.filter(user=attrs)
        if attrs.role != CustomUser.BORROWER_ROLE_CODE:
            raise serializers.ValidationError('Please Select Borrower User')
        

