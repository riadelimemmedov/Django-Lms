

#Django 
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.contrib.auth.models import User

#Imported Models
from book.models import *
from library.models import *

# Create your models here.

#!BorrowedUser
class BorrowedUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50,blank=True)
    lastname = models.CharField(max_length=50,blank=True)
    email_address = models.EmailField(max_length=50,unique=True,blank=False)
    age = models.PositiveIntegerField(blank=True,default=0)
    slug = models.SlugField(unique=True,db_index=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    borrowed_books = models.ManyToManyField(Book,related_name='borrowed_user',blank=True)
    borrowed_library = models.ForeignKey(Library,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args,**kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'BorrowedUser'
        verbose_name_plural = 'BorrowedUsers'

#?Create BorrowedUser Objects after creating User model
def create_borrowed_user_profile_for_user(sender,instance,created,**kwargs):
    if created:
        BorrowedUser.objects.create(user=instance)
post_save.connect(create_borrowed_user_profile_for_user,sender=User)