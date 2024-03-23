from django.shortcuts import render, redirect
from .helper import *

# Create your views here.
def index(request):
    return redirect('home')
def home(request):
    return render(request, 'main/home.html', {'active_tab': 'home'})
def career(request):
    return redirect('workX')
def education(request):
    return render(request, 'main/career/education.html', {'active_tab': 'career'})
def workX(request):
    return render(request, 'main/career/workX.html', {'active_tab': 'career'})
def about(request):
    return render(request, 'main/about.html', {'active_tab': 'about'})
def skills_and_projects(request):
    return redirect('projects')
def skills(request):
    return render(request, 'main/skills-and-projects/skills.html', {'active_tab': 'skills-projects'})
def projects(request):
    return render(request, 'main/skills-and-projects/projects.html', {'active_tab': 'skills-projects'})
def services(request):
    return render(request, 'main/services.html', {'active_tab': 'services'})
def contact(request):
    return render(request, 'main/contact.html', {'active_tab': 'contact'})
def socials(request):
    socials = [
        {
            'id': 1,
            'name': 'LinkedIn',
            'url': 'https://www.linkedin.com/in/aadilsehrawat/',
            'social_image_url': 'images/socials/black-on-white/linkedin.png'
        },
        {
            'id': 2,
            'name': 'GitHub',
            'url': 'https://www.github.com/aadilsehrawat/',
            'social_image_url': 'images/socials/black-on-white/github.png'
        },
        {
            'id': 3,
            'name': 'Instagram',
            'url': 'https://www.instagram.com/aadilsehrawat/',
            'social_image_url': 'images/socials/black-on-white/instagram.png'
        },
        {
            'id': 4,
            'name': 'Facebook',
            'url': 'https://www.facebook.com/aadilsehrawat/',
            'social_image_url': 'images/socials/black-on-white/facebook.png'
        },
        {
            'id': 5,
            'name': 'LeetCode',
            'url': 'https://www.leetcode.com/aadilsehrawat/',
            'social_image_url': 'images/socials/black-on-white/leetcode.png'
        },
        {
            'id': 6,
            'name': 'Twitter',
            'url': 'https://www.twitter.com/aadilsehrawat/',
            'social_image_url': 'images/socials/black-on-white/twitter.png'
        },
    ]
    context = {
        'active_tab': 'socials',
        'socials': socials,
    }
    # if ('LeetCode' in [social['name'] for social in socials]):
        # leetcode_data = get_leetcode_data()
        # if leetcode_data:
            # context['leetcode_data'] = leetcode_data
    return render(request, 'main/socials.html', context)