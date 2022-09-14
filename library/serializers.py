#Rest Framework
from rest_framework import serializers

#Django Models and Function
from .models import Library
from custom_user.models import CustomUser


#!LibrarySerializer
class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'
        

#!RegisterLibrarianSerializer
class RegisterLibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','password']