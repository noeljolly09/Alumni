from django.db import models
from django.contrib.auth.models import User

class Applicant(models.Model):

    genderchoice = (('male','MALE'),('female','FEMALE'))


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=10)

    image = models.ImageField(blank=True, null=True, upload_to="applicant_profile_images/",default='default.jpg')

    gender = models.CharField(choices=genderchoice,max_length=8)

    type = models.CharField(max_length=15)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Company(models.Model):

    genderchoice = (('male','MALE'),('female','FEMALE'))
    status = (('accepted','Accepted'),('pending','Pending'),('rejected','Rejected'))


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=10)

    image = models.ImageField(blank=True, null=True, upload_to="company_logo/")

    gender = models.CharField(choices=genderchoice,max_length=8)

    type = models.CharField(max_length=15)

    status = models.CharField(choices=status, max_length=10)

    company_name = models.CharField(max_length=100)

    def __str__ (self):
        return self.company_name

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    start_date = models.DateField()

    end_date = models.DateField()

    title = models.CharField(max_length=200)

    salary = models.FloatField()

    description = models.TextField(max_length=400)

    experience = models.CharField(max_length=100)
    
    location = models.CharField(max_length=100)

    skills = models.CharField(max_length=200)

    creation_date = models.DateField()

    def __str__ (self):
        return self.title

class Application(models.Model):
    company = models.CharField(max_length=200, default="")

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    resume = models.ImageField(upload_to="applicant_resume/",default ='default.jpg')
    
    apply_date = models.DateField()

    def __str__ (self):
        return str(self.applicant)