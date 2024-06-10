from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
    video = EmbedVideoField()

class Patient(models.Model):
    firstName = models.CharField(max_length=100,blank=False,null=False )
    lastName = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField()
    gender = models.CharField(max_length=10,blank=False,null=False)
    age = models.IntegerField()
    city = models.CharField(max_length=10,blank=False,null=False)
    phone = models.CharField(max_length=8,blank=False,null=False)
    allergies = models.CharField(max_length=100,null=True)
    medications = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,blank=False,null=False)
    time = models.CharField(max_length=100,blank=False,null=False)
    def __str__(self):
        return self.firstName
class Avis(models.Model):
    firstName=models.CharField(max_length=20,blank=False,null=False)
    lastName=models.CharField(max_length=20,blank=False,null=False)
    avis=models.CharField(max_length=200,blank=False,null=False)
    image=models.ImageField(upload_to="images/")
    def __str__(self):
        return f"{self.firstName} {self.lastName}"