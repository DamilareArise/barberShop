from django.shortcuts import render,redirect, get_object_or_404
from .models import Booking
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, AdminResponseForm
from django.contrib import messages
from barberShop.serviceApp.models import SubService
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import transaction
# Create your views here.

@login_required
def view_bookings(request,userid):
    if request.user.is_superuser:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(user_id = userid)
    return render(request, 'bookingApp/view_bookings.html',{'bookings':bookings})

@transaction.atomic()
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
    
@transaction.atomic()
@login_required
def adminResponse(request, book_id):
    booking = get_object_or_404(Booking, booking_id = book_id)
    if request.method == 'POST':
        response_form = AdminResponseForm(request.POST, request.FILES, instance = booking)
        if response_form.is_valid():
            response_form.save()
            messages.success(request, 'Response has been successfully created')

            send_mail(
            'Booking Response',# Subject of the mail
            f'Dear {booking.service.service.HOD.user.first_name}, You\'ve responded to booking ID-{book_id} ', # Body of the mail
            'barberShop@gmail.com', # From email (Sender)
            [booking.service.service.HOD.user.email], # To email (Receiver)
            fail_silently=False, # Handle any error
            )

            send_mail(
            'Booking Response',# Subject of the mail
            f'Hi {booking.user.first_name}, Your appointment has been received. Awaiting confirmation, visit your dashboard', # Body of the mail
            'barberShop@gmail.com', # From email (Sender)
            [booking.user.email], # To email (Receiver)
            fail_silently=False, # Handle any error
            )
        return view_bookings(request, request.user.id)
    else:
        response_form = AdminResponseForm(instance = booking)
        return render(request, 'bookingApp/create_booking.html', {'response_form': response_form})

@login_required       
def deleteBooking(request, book_id):
    booking = get_object_or_404(Booking, booking_id = book_id)
    booking.delete()
    messages.success(request, 'Booking has been successfully deleted')
    send_mail(
    'Booking Delete Alert',# Subject of the mail
    f'Dear {booking.service.service.HOD.user.first_name}, Booking ID-{book_id} deleted', # Body of the mail
    'barberShop@gmail.com', # From email (Sender)
    [booking.service.service.HOD.user.email], # To email (Receiver)
    fail_silently=False, # Handle any error
    )

    send_mail(
    'Booking Delete Alert',# Subject of the mail
    f'Hi {booking.user.first_name}, Booking ID-{book_id} deleted', # Body of the mail
    'barberShop@gmail.com', # From email (Sender)
    [booking.user.email], # To email (Receiver)
    fail_silently=False, # Handle any error
    )
    return view_bookings(request, request.user.id)