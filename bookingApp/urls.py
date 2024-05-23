from django.urls import path
from .views import *

urlpatterns = [
    path('create_booking/<int:subServ_id>/', create_booking, name="create_booking"),
    path('view_bookings/<int:userid>/', view_bookings, name="view_bookings"),
    path('admin_response/<int:book_id>/',adminResponse, name='admin_response'),
    path('delete_booking/<int:book_id>/', deleteBooking, name='delete_booking')
]