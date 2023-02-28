from django.db import models
from flights.models import Flight
# Create your models here.


class Reservations(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    num_people = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

class Tickets(models.Model):
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    MAIN_CABIN = 'M'
    TICKET_CHOICES = [
        (FIRST_CLASS, 'First Class'),
        (BUSINESS_CLASS, 'Business Class'),
        (MAIN_CABIN, 'Main Cabin'),
    ]
    reservation = models.ForeignKey(Flight, on_delete=models.PROTECT)
    seat = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_class = models.CharField(
        max_length=1,
        choices=TICKET_CHOICES
    )
