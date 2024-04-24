from django.urls import path
# from barberShop.userApp import views as userView
from .views import *


urlpatterns = [
    path("my_account/<int:userid>/", my_account, name="my_account"),
    path('edit_admin/<int:userid>/', edit_Adminprofile, name="edit_admin"),
    path('edit_user/<int:userid>/', edit_Userprofile, name="edit_user"),
    path('display-user/<str:user>/', allUser, name='display-user'),
    path('deactivate-user/<int:userid>/', deactivate_account, name='deactivate-user'),

]
