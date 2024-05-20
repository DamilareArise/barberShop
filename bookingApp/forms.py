from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'booking_date',
            'booking_time'
        ]

        widgets = {
            'booking_date': forms.NumberInput(attrs={'type':'date'}),
            'booking_time': forms.NumberInput(attrs={'type':'time'})
        }
