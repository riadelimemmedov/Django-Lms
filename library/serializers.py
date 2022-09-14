#Rest Framework
from rest_framework import serializers

#Django Models and Function
from .models import *


#!LibrarySerializer
class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'