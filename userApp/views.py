from django.shortcuts import render
from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# Create your views here.


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'


@login_required
def my_account(request, userid):
    # Profile.objects.only("address", "email").filter(profile_id=userid) #selecting only this columns from the database
    # Profile.objects.exclude("address", "email").filter(profile_id=userid) #selecting all aside the ones selescted
    # Profile.objects.all() #selecting all the details in the database

    profile = UserProfile.objects.all().filter(user_id = userid)
    print(profile)
    return render(request=request, template_name='userApp/my_account.html', context={"userprofile":profile})