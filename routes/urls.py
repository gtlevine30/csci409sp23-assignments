# Load path from django.urls
from django.urls import path
# Load this applications views.py file
from . import views

# Define url patterns
urlpatterns = [
    path('/', views.route_search),

    path('/search/<str:origin>/<str:destination>', views.route_search),
]