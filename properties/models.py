from django.db import models
import uuid
from django.urls import reverse
import boto3
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.

class Property(models.Model):
    id = models.UUIDField( 
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    projStatus = models.CharField(max_length=50,null=True)
    propertyImage1 = models.ImageField(
        null=True,blank=True,upload_to='media/')
    propertyImage2 = models.ImageField(
        null=True,blank=True,upload_to='media/')
    propertyImage3 = models.ImageField(
        null=True,blank=True,upload_to='media/')
    projectName = models.CharField(max_length=50)
    projectType = models.CharField(max_length=50,default=None)
    address = models.CharField(max_length=1100)
    directions = models.URLField(default=None)
    developmentSize = models.FloatField(default=None)
    noOfUnits = models.IntegerField(default=None)
    bedrooms = models.CharField(max_length=50,default=None)
    about = models.TextField(default=None)
    unitPlan1 = models.ImageField(blank=True,upload_to='media/')
    unitPlan2 = models.ImageField(blank=True,upload_to='media/')
    structure = models.TextField(default=None)
    lobby = models.TextField(default=None)
    lifts = models.TextField(default=None)
    apartmentFlooring = models.TextField(default=None)
    kitchen = models.TextField(default=None)
    utility = models.TextField(default=None)
    toiletsNFittings = models.TextField(default=None)
    painting = models.TextField(default=None)
    doorsNWindows = models.TextField(default=None)
    electrical = models.TextField(default=None)
    securitySystem = models.TextField(default=None)
    dgBackup = models.TextField(default=None)

    def __str__(self):
        return self.projectName[:50]

    def s1(self):
        if self.structure:
            return self.structure.split('.')
        else:
            return None

    def s2(self):
        if self.lobby:
            return self.lobby.split('.')
        else:
            return None

    def s3(self):
        if self.lifts:
            return self.lifts.split('.')
        else:
            return None

    def s4(self):
        if self.apartmentFlooring:
            return self.apartmentFlooring.split('.')
        else:
            return None

    def s5(self):
        if self.kitchen:
            return self.kitchen.split('.')
        else:
            return None

    def s6(self):
        if self.utility:
            return self.utility.split('.')
        else:
            return None

    def s7(self):
        if self.toiletsNFittings:
            return self.toiletsNFittings.split('.')
        else:
            return None

    def s8(self):
        if self.painting:
            return self.painting.split('.')
        else:
            return None

    def s9(self):
        if self.doorsNWindows:
            return self.doorsNWindows.split('.')
        else:
            return None

    def s10(self):
        if self.electrical:
            return self.electrical.split('.')
        else:
            return None

    def s11(self):
        if self.securitySystem:
            return self.securitySystem.split('.')
        else:
            return None

    def s12(self):
        if self.dgBackup:
            return self.dgBackup.split('.')
        else:
            return None

    def get_absolute_url(self):
        return reverse('property',args=[str(self.id)])
        
        
@receiver(models.signals.post_delete, sender=Property)
def remove_file_from_s3(sender, instance, using, **kwargs):
    image_fields = ['propertyImage1', 'propertyImage2', 'propertyImage3', 'unitPlan1', 'unitPlan2']
    for field_name in image_fields:
        # Get the image field value
        image_field = getattr(instance, field_name)
        if image_field:
            # Delete the image file
            image_field.delete(save=False)
                