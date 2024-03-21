from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('home')
def home(request):
    return render(request, 'main/home.html')
def about(request):
    return render(request, 'main/about.html')
def projects(request):
    return render(request, 'main/projects.html')
def services(request):
    return render(request, 'main/services.html')
def contact(request):
    return render(request, 'main/contact.html')