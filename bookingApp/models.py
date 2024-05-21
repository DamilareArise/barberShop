from django.db import models
from barberShop.serviceApp.models import SubService
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    status = [
        ('Pending', 'Pending'), 
        ('Confirmed', 'Confirmed'), 
        ('Completed', 'Completed'), 
        ('Cancelled', 'Cancelled')
    ]

    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(SubService, on_delete=models.CASCADE)
    booking_date = models.DateField(null=True, blank=True, unique=False)
    booking_time = models.TimeField(null=True, blank=True, unique=False)
    approved_date = models.DateField(null=True, blank=True, unique=False)
    approved_time = models.TimeField(null=True, blank=True, unique=False)
    status = models.CharField(
        max_length=20, 
        choices= status,
        default='Pending'
    )
    payment_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return F'{self.booking_id}--{self.user.email}'