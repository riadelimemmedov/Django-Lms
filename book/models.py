
#Django Models and Function
from django.db import models
from django.utils.text import slugify

#Python Module
import random

# Create your models here.

#!Book
class Book(models.Model):
    name = models.CharField(max_length=50,blank=False)
    author = models.CharField(max_length=50,blank=False)
    page_number = models.PositiveIntegerField(blank=False)
    slug = models.SlugField(unique=True,db_index=True,blank=True)
    product_code = models.CharField(max_length=15,blank=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
    def save(self, *args, **kwargs):
        #?Save Slug
        self.slug = slugify(self.name)
        
        #?Generate Random Number
        number_range = [i for i in range(1000)]
        code_list = []
        for item in range(4):
            number = random.choice(number_range)
            code_list.append(number)
        code_string = ''.join(str(data) for data in code_list)
        self.product_code = code_string
        super().save(*args,**kwargs)
        