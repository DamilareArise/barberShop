from django.db import models
from barberShop.userApp.models import UserProfile



# Create your models here.
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    HOD =   models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    service_image = models.ImageField(upload_to='service-image/', blank=True, null=True, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class SubService(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    subService_image = models.ImageField(upload_to='sub-service-image/', blank=True, null=True, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name