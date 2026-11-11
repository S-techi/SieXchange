from django.shortcuts import render, redirect
from . models import *

# Create your views here.
def error(request):
    return render(request, '404.html')

def blogDetails(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def index(request):
    if request.method == 'POST' :
        mycontact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontact.save()
        return redirect('/')
    else:
        return render(request, 'index.html')
    

def portfolioDetails(request):
    return render(request, 'portfolio-details.html')

def serviceDetails(request):
    return render(request, 'service-details.html')

def starterPage(request):
    return render(request, 'starter-page.html')

def show(request):
    all = Contact.objects.all()
    return render(request, 'show.html', {"all" : all})