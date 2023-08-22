from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
class Applicants(models.Model):
    firstname= models.CharField(max_length=10,default="hh")
    lastname=models.CharField(max_length=10)
    username=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    email=models.EmailField(max_length=20)
    phone=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    profile=models.ImageField(upload_to="",default=None)
    resume =models.FileField(upload_to="upload",default=None)
    
    

    def __str__(self):
        return self.firstname

  
class Company(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email =models.EmailField(max_length=20)
    company_name=models.CharField(max_length=100)
    address=models.CharField(max_length=20,default="kochi")
    type=models.CharField(max_length=20,default="it")
    location=models.CharField(max_length=20,default="kochi")
    logo=models.ImageField(upload_to="",default=None)

    def __str__(self):
        return self.company_name


class Job (models.Model):
    
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    start_date =models.DateTimeField(auto_now_add=True,null=True)
    end_date =models.DateTimeField(auto_now_add=True,null=True)
    title =models.CharField(max_length=100,default="",blank=True,null=True)
    salary =models.FloatField(default=0.0,blank=True,null=True)
    description =models.TextField(max_length=500,default=None,blank=True,null=True)
    experience = models.CharField(max_length=60,default="",blank=True,null=True)
    location =models.CharField(max_length=200,default="",blank=True,null=True)
    skills =models.CharField(max_length=200,default="",blank=True,null=True)
    vacancy=models.IntegerField(default=0,blank=True,null=True)
    qualification=models.CharField(max_length=50,default="",blank=True,null=True)
    creation_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
    
class Application(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,)
    job=models.ForeignKey(Job,on_delete=models.CASCADE,related_name='jobs')
    applicant =models.ForeignKey(Applicants,on_delete=models.CASCADE,related_name='applicant')
    resume =models.FileField()
    apply_date=models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.applicant)