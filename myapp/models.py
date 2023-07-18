from django.db import models
from datetime import date


class User(models.Model):
    username=models.CharField('User Name',max_length=100)
    email=models.CharField('email',max_length=30)
    password=models.CharField('password ',max_length=12)

class Mainproperty(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    title=models.CharField('Post Title',max_length=100)
    details=models.CharField('Post Details',max_length=1000)
    PostDate=models.DateField(default=date.today)
    WriterName=models.CharField('Write Name',max_length=100)

class Contactus(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Firstname = models.CharField(' First name', max_length=100)
    Lastname = models.CharField(' last name', max_length=100)
    email = models.CharField('email', max_length=100)
    subject = models.CharField('subject', max_length=100)
    message = models.CharField('message', max_length=100)

class Service(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    FullName = models.CharField('FullName', max_length=100)
    email = models.CharField('email', max_length=100)
    City = models.CharField('City', max_length=100)
    ApartmentSize = models.CharField('ApartmentSize', max_length=100)
    message = models.CharField('message', max_length=100)

