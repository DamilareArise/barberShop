from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]

    countries = [
        ('Nigeria', 'Nigeria'),
        ('United State', 'United State'),
        ('Others', 'Others')
    ]

    departments = [
        ('Admin','Admin'),
        ('Supervisor','Supervisor'),
        ('Hair Cut Specialist', 'Hair Cut Specialist'),
        ('Beard Specialist', 'Beard Specialist'),
        ('Hair Color Specialist','Hair Color Specialist')
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    gender = models.CharField(choices=gender, max_length=50)
    date_of_birth =  models.CharField(max_length=11)
    portfolio = models.FileField(upload_to ='portfolio/', unique=False, null=True)
    nationality = models.CharField(choices=countries, max_length=20)
    displayPicture = models.ImageField(upload_to='profile_picture/', unique=False, null=True)
    department = models.CharField(choices=departments, max_length=255)
    staff = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
