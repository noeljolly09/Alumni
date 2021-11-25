
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.urls import reverse



class branchData(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('homepage')

class courseData(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
        
    def get_absolute_url(self):
        return reverse('homepage')


class alumniData(models.Model):
    
    genderchoice = (('unknown','UNKNOWN'),('male','MALE'),('female','FEMALE'))

    
    Name = models.CharField(max_length=25)
    Bio = models.CharField(max_length=100, default='Here is My Bio')
    Profile_image = models.ImageField(blank=True, null=True, upload_to="profile_images/",default='default.jpg')
    Email = models.ForeignKey(User, on_delete=models.CASCADE)
    Gender = models.CharField(choices=genderchoice,max_length=8,default='unknown')
    Birthdate = models.DateField(blank=True,null=True)
    Designation = models.CharField(max_length=50, default='Software Developer')
    Phone_number = models.CharField(max_length=10)
    Address = models.TextField(max_length=120,blank=True,null=True)
    Course = models.ForeignKey(courseData, on_delete=models.CASCADE,blank=True,null=True)
    Branch = models.ForeignKey(branchData, on_delete=models.CASCADE,blank=True,null=True)
    BatchYear = models.CharField(max_length=4,default=0)

    def __str__(self):
        return self.Name + ' ----> ' + str(self.BatchYear) + ' Batch'

    def get_absolute_url(self):
        return reverse('alumnidirectory')


class gallery(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True, upload_to="gallery_images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery')