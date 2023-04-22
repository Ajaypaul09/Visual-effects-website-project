import requests
from django.http import HttpResponse
from django.shortcuts import render
from .models import Animation
from .models import Contacts
from .models import Register
from .models import News


def index(request):
    animations=Animation.objects.all()
    return render(request, 'index.html', {'animations':animations})


def new(request):
    return HttpResponse('new products')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def indexx(request):
    return render(request,'index.html')




def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')


def contacts(request):
    if request.method == 'POST':
        email_r=request.POST.get('email')
        number_r = request.POST.get('number')
        name_r = request.POST.get('name')
        message_r = request.POST.get('message')
        address_r=request.POST.get('address')
        c = Contacts(email=email_r,number=number_r,name=name_r,message=message_r,address=address_r)
        c.save()
        return render(request, 'index.html')
    else:
        return render(request, 'contact.html')
       # print("error occured")


def register(request):
    if request.method == 'POST':
        email_r=request.POST.get('email')
        number_r = request.POST.get('number')
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        c = Register(email=email_r,number=number_r,name=name_r,password=password_r)
        c.save()
        return render(request, 'index.html')
    else:
        return render(request, 'register.html')
       # print("error occured")


def news(request):
    if request.method == 'POST':
        email_r=request.POST.get('email')
        c= News(email=email_r)
        c.save()
        return render(request, 'index.html')
    else:
        return render(request,'#')







