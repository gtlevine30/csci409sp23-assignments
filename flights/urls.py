# Load path from django.urls
from django.urls import path
# Load this applications views.py file
from . import views

# Define url patterns
urlpatterns = [
    path('/', views.flight_search),

    path('/search/<str:origin>/<str:destination>', views.flight_search),
]