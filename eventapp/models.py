from django.db import models

class Service(models.Model):
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name = models.CharField("Customer Name", max_length=55)
    cus_ph = models.CharField("Phone Number", max_length=12)
    type = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Event Type")
    booking_date = models.DateField("Preferred Booking Date")
    booked_on = models.DateField("Booking Created On", auto_now=True)

    def __str__(self):
        return f"{self.cus_name} - {self.type.name}"





