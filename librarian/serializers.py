#Rest Framework
from rest_framework import serializers

#Django Models and Function
from .models import *

#!LibrarianSerializer
class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'