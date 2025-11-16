from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Service
from .forms import BookingForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Prepare email content
            subject = f"New Booking from {booking.cus_name}"
            message = f"""
You have received a new booking on CELEBYTE:

Name: {booking.cus_name}
Phone: {booking.cus_ph}
Event Type: {booking.type}
Booking Date: {booking.booking_date}
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = ['your_email@gmail.com']  # 🔁 Replace with your admin email

            # Send the email
            send_mail(subject, message, from_email, to_email, fail_silently=False)

            messages.success(request, "Thank you! Our team will contact you soon.")
            return redirect('booking')

    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'ser': services})









