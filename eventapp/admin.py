from django.contrib import admin
from .models import Service, Booking
from django.utils.html import format_html

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'preview_image']
    search_fields = ['name', 'desc']

    def preview_image(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="height:50px;"/>', obj.img.url)
        return "-"
    preview_image.short_description = "Image"

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['cus_name', 'cus_ph', 'type', 'booking_date', 'booked_on']
    list_filter = ['booking_date', 'booked_on']
    search_fields = ['cus_name', 'cus_ph']







