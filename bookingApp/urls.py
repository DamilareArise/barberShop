from django.urls import path
from .views import *

urlpatterns = [
    path('view_bookings/<int:userid>/', view_bookings, name="view_bookings"),
    path('create_booking/<int:subServ_id>/', create_booking, name="create_booking")
]