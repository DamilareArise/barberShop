from django import forms
from .models import *
from barberShop.userApp.models import UserProfile


class ServiceForm(forms.ModelForm):
    HOD = forms.ModelChoiceField(queryset=UserProfile.objects.filter(HOD=True), empty_label=None,label='Head of Department', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Service
        fields = [
            'name',
            'description',
            'service_image',
            'HOD'
        ]

class SubServiceForm(forms.ModelForm):
    
    class Meta:
        model = SubService
        fields = [
            'name',
            'subService_image',
            'price'
        ]