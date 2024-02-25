from django.db import models

#Create your models here.

class Enquire(models.Model):
    projectName = models.CharField(max_length=50,null = True)
    custName = models.CharField(max_length=50,null = True)
    custPhone = models.CharField(max_length=50,null = True)
    custEmail = models.CharField(max_length=50,null = True)
    custMessage = models.TextField(max_length=50,null = True)

    def __str__(self):
        return self.custName[:50]


