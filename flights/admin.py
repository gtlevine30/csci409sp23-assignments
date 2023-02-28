from django.contrib import admin
from .models import Flight, Airline

# Register your models here.
class Airlines(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['airline_name', 'airport_code']}),
        ('departure_and_arrival_time', {'fields': ['origin', 'destination'], 'classes': ['collapse']})
    ]

admin.site.register(Flight, Airlines)
