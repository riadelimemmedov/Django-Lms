#Django 
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

#Imported Models
from book.models import *
from library.models import *



# Create your models here.
#!Librarian
class Librarian(models.Model):
    firstname = models.CharField(max_length=50,blank=False)
    lastname = models.CharField(max_length=50,blank=False)
    working_library = models.ForeignKey(Library,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.firstname} --- {self.lastname}"
    
    class Meta:
        verbose_name = 'Librarian'
        verbose_name_plural = 'Librarians'