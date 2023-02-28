from django.http import HttpResponse

def flight_search(request, origin, destination):
    return HttpResponse('Showing flights from ' + origin + ' to ' + destination);