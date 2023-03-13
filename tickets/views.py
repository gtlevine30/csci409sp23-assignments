from django.http import HttpResponse
from .models import Reservations

def index(request):
    # Nothing to do here
    return HttpResponse('Hello from tickets')

def ticket_search(request, confirmation_number):
    # Select the singular reservation for the confirmation number
    # Note: the confirmation_number is the id in the Reservation table
    reservation = Reservations.objects.get(airport_code=confirmation_number)
    return HttpResponse('Number of tickets for confirmation number: ' + str(confirmation_number) + " is " + str(reservation.num_people))