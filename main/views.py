from django.shortcuts import render, redirect
from .helper import *
from . import data, home_data

# Create your views here.
def index(request):
    return redirect('home')
def home(request):
    context={
        'active_tab': 'home',
        'skills': home_data.featured_skills,
        'latest_education': home_data.latest_education,
        'latest_experience': home_data.latest_experience,
    }
    return render(request, 'main/home.html', context)
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
    skills_by_category = {}
    for skill in data.skills:
        category = skill['category']
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    context = {
        'active_tab': 'skills-projects',
        'skills_by_category': skills_by_category,
    }
    return render(request, 'main/skills-and-projects/skills.html', context)
def projects(request):
    for index, item in enumerate(data.projects, start=1):
        item['position'] = index
    context = {
        'active_tab': 'skills-projects',
        'projects': data.projects,
    }
    return render(request, 'main/skills-and-projects/projects.html', context)
def services(request):
    for index, item in enumerate(data.services, start=1):
        item['position'] = index
    context = {
        'active_tab': 'services',
        'services': data.services,
    }
    return render(request, 'main/services.html', context)
def contact(request):
    return render(request, 'main/contact.html', {'active_tab': 'contact'})
def socials(request):
    for index, item in enumerate(data.socials, start=1):
        item['position'] = index
    context = {
        'active_tab': 'socials',
        'socials': data.socials,
    }
    # if ('LeetCode' in [social['name'] for social in socials]):
        # leetcode_data = get_leetcode_data()
        # if leetcode_data:
            # context['leetcode_data'] = leetcode_data
    return render(request, 'main/socials.html', context)