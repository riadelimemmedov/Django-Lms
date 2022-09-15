#Rest Framework
from rest_framework import serializers

#Django Models and Function
from .models import Book


#!BookSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name','author','page_number']