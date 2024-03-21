from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('socials/', socials, name='socials'),
]