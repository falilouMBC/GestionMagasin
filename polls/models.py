from audioop import reverse
from msilib.schema import Property
from django.urls import reverse
from distutils.command.upload import upload
from enum import unique
from pyexpat import model
from random import choices
from statistics import mode
from django.db import models
from django.conf import settings
from django import forms
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveBigIntegerField(default=0)
    sex = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse('update', kwargs={'pk':self.id})



class PersonForm(forms.Form):
    pass

class Market(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updatd_at  = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=200, choices = settings.COUNTRIES)
    
    class Meta:
        abstract = True
        ordering = ['name',]
    
    def __str__(self):
        return self.name

class Magasin(Market):  
    pass
    
        
class Produit(Market):
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to = "PRODUCT_IMG")
    magasin = models.OneToOneField(Magasin,
                                   on_delete=models.CASCADE,
                                   related_name="product_magasin")

class ProfilMagasin(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    phone = models.CharField (max_length=30,unique=True)
    magasin = models.OneToOneField(Magasin,
                                   on_delete=models.CASCADE,
                                   related_name="magasin_profile") 
    created_at = models.DateTimeField(auto_now_add=True)
    updatd_at  = models.DateTimeField(auto_now=True)



@property
def majeur(self):
    return 'Majeur' if self.age > 18 else 'Mineur'