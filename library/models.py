
#Django Models and Function
from django.db import models

#Imported Models
# from borrower.models import BorrowedUser
# from book.models import Book

# Create your models here.

#!Library
class Library(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'