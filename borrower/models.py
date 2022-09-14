

#Django 
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User

#Imported Models
from book.models import *
from library.models import *

# Create your models here.

#!BorrowedUser
class BorrowedUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=50,blank=True)
    lastname = models.CharField(max_length=50,blank=True)
    email_address = models.EmailField(max_length=50,blank=False)
    age = models.PositiveIntegerField(blank=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    borrowed_books = models.ManyToManyField(Book,related_name='borrowed_user',blank=True)
    borrowed_library = models.ForeignKey(Library,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.user)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'BorrowedUser'
        verbose_name_plural = 'BorrowedUsers'

#?Create BorrowedUser Objects after creating User model
# def create_borrowed_user_profile_for_user(sender,instance,created,**kwargs):
#     if created:
#         BorrowedUser.objects.create(user=instance)
# post_save.connect(create_borrowed_user_profile_for_user,sender=User)