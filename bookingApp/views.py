from django.shortcuts import render,redirect, get_object_or_404
from .models import Booking
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.contrib import messages
from barberShop.serviceApp.models import SubService
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.

@login_required
def view_bookings(request,userid):
    bookings = Booking.objects.filter(user_id = userid)
    return render(request, 'bookingApp/view_bookings.html',{'bookings':bookings})


@login_required
def create_booking(request,subServ_id):
    sub_service = get_object_or_404(SubService, id = subServ_id)
    user = get_object_or_404(User, id = request.user.id)
    if request.method == 'POST':
        booking_form = BookingForm(request.POST, request.FILES )
        if booking_form.is_valid():
            form = booking_form.save(commit=False)
            form.user = user
            form.service = sub_service
            form.save()
            messages.success(request, 'Booking has been successfully created')

            send_mail(
            'Booking has been made by a client',# Subject of the mail
            f'Dear Hod. {sub_service.service.HOD.user.first_name}, a client has booked a service. Please do a proper follow up ', # Body of the mail
            'barberShop@gmail.com', # From email (Sender)
            [sub_service.service.HOD.user.email], # To email (Receiver)
            fail_silently=False, # Handle any error
            )

            send_mail(
            'Booking Recieved',# Subject of the mail
            f'Dear Sir/Ma {user.first_name}, Your appointment has been recieved. Await confirmation', # Body of the mail
            'barberShop@gmail.com', # From email (Sender)
            [user.email], # To email (Receiver)
            fail_silently=False, # Handle any error
            )
        return view_bookings(request, user.id)
    else:
        booking_form = BookingForm()
        return render(request, 'bookingApp/create_booking.html', {'booking_form': booking_form})