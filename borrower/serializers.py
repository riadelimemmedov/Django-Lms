#Rest Framework
from rest_framework import serializers

#Django Models and Function
from .models import *

#!BorrowerSerializer
class BorrowerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    borrowed_books = serializers.StringRelatedField(read_only=True,many=True)
    borrowed_library = serializers.CharField(read_only=True)
    class Meta:
        model = BorrowedUser
        fields = ['id','user','borrowed_books','borrowed_library']
