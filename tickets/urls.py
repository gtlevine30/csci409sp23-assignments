# Load path from django.urls
from django.urls import path
# Load this applications views.py file
from . import views

# Define url patterns
urlpatterns = [
    path('/', views.ticket_search),

    path('/<confirmation_number>', views.ticket_search),
]