from django.urls import path
# from barberShop.userApp import views as userView
from .views import *


urlpatterns = [
    path("my_account/<int:userid>/", my_account, name="my_account")
]
