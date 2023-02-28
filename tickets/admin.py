from django.contrib import admin
from .models import Reservations, Tickets

# Register your models here.

class TicketInline(admin.StackedInline):
    model = Tickets
    extra = 2

class ReservationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['flights', 'num_people', 'total_cost']})
    ]

    inlines = [TicketInline]

admin.site.register(Reservations, ReservationAdmin)




