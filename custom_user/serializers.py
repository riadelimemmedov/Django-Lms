from rest_framework import serializers
from .models import *


#!RegisterCustomUser
class RegisterCustomUser(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20,style={'input_type':'text','placeholder':'Input Username'},required=True)
    password = serializers.CharField(max_length=16,style={'input_type':'password','placeholder':'Input Password'},required=True)
    email = serializers.EmailField(max_length=20,style={'placeholder':'Input Email'},required=True)
    
    
    class Meta:
        model = CustomUser
        fields = ['username','password','email']
        
        
