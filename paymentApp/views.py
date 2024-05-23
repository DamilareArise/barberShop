from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.core.mail import send_mail
from barberShop.bookingApp.models import Booking
from .models import Payment_service
# Create your views here.
@login_required
def bookingPayment(request, book_id):
    pass


@login_required
def failPayment(request, userid):
    messages.error(request, ('Your payment Fails!'))

    return redirect('view_bookings', userid)

@transaction.atomic
@login_required
def successPayment(request, book_id):
    booking = Booking.objects.get(booking_id=book_id)

    payment = Payment_service(user_id = request.user.id, booking_id = book_id, amount = booking.price)
    payment.save()

    payment = Booking.objects.filter(booking_id=book_id).update(payment_status=True)

    send_mail(
            'Payment Confirmed',
            f'Hi {booking.user.first_name}, Your booking has been approved. see your booking details for more information',
            'techcare@gmail.com',
            [booking.user.email],
            fail_silently=False,
        )

    messages.success(request, ('Your payment was successful'))
    return redirect('view_bookings', request.user.id)
