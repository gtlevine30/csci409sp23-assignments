from django.http import HttpResponse

def route_search(request, origin, destination):
    return HttpResponse('Showing routes from ' + origin + ' to ' + destination);