#Rest Framework
from rest_framework import serializers

#Django Models and Function
from .models import *
from custom_user.models import CustomUser
from library.models import *
from library.serializers import LibrarySerializer

#!BorrowerSerializers
class BorrowerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    borrowed_library = LibrarySerializer(read_only=True)
    
    class Meta:
        model = BorrowedUser
        fields = ['id','user','borrowed_books','borrowed_library']
        depth=1
        
    
    def validate_user(self, attrs):
        custom_user = BorrowedUser.objects.filter(user=attrs)
        if attrs.role != CustomUser.BORROWER_ROLE_CODE:
            raise serializers.ValidationError('Please Select Borrower User')
        elif custom_user:
            print('hardadu anj yser ',custom_user)
            raise serializers.ValidationError('This Borrower User Already Exist')

        print('user value ', attrs.role)

