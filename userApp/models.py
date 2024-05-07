from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    profile_id = models.AutoField(primary_key=True)
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
    HOD =  models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()