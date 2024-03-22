from django.shortcuts import render, redirect

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
    return render(request, 'main/socials.html', {'active_tab': 'socials'})