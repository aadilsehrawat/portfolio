from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('career/', career, name='career'),
    path('career/education/', education, name='education'),
    path('career/work/', workX, name='workX'),
    path('about/', about, name='about'),
    path('skills-and-projects/', skills_and_projects, name='skills-projects'),
    path('skills-and-projects/skills/', skills, name='skills'),
    path('skills-and-projects/projects/', projects, name='projects'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('socials/', socials, name='socials'),
]