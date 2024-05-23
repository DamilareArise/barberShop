from django.db import models
from barberShop.bookingApp.models import Booking
from django.contrib.auth.models import User

# Create your models here.

class Payment_service(models.Model):

    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, unique=False, on_delete=models.CASCADE )
    booking = models.ForeignKey(Booking, null=False, unique=False, on_delete=models.CASCADE )
    amount = models.BigIntegerField(unique=False, null= False)
    date_of_payment = models.DateTimeField(auto_now_add=True, null=False)
    paystack_detail = models.BigIntegerField(unique=True, null=False)

    def __str__(self) -> str:
        return f'Payment -ID-0-{self.payment_id}'