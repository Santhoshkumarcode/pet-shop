from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.conf import settings
from .models import *
# Create your views here.
 
def landing(request):

    return render(request,"landingpage.html")

def reg(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        number = request.POST.get('number')
        my_user = User.objects.create_user(username=uname, email=email, password=password)
        my_user.number = number 
         # Assuming 'number' is a field in your custom user model
        my_user.save()
        return redirect('landing') 
    return render(request, "register.html")

def log(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass1')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('landing')
        else:
            return HttpResponse('<h1>user name or password wrong</h1>')
    return render(request,"login.html")

def adopt(request):
    details=puppydetails.objects.all()
    return render(request,"adopt.html",{'details':details})

def donate(request): 
    if request.method=='POST':
        name=request.POST.get('name')
        breed=request.POST.get('breed')
        age=request.POST.get('age')
        vac=request.POST.get('vaccination')
        number=request.POST.get('number')
        print(vac)
        obj=puppydetails()
        obj.name=name
        obj.breed=breed
        obj.age=age
        obj.vaccination=vac
        obj.number=number
        obj.save()
        return render(request, "donated.html")

    return render(request,"donate.html")

def buy(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        breed=request.POST.get('breed')
        quantity=request.POST.get('quantity')
        number=request.POST.get('number')

        obj=customerdetails()
        obj.name=name
        obj.email=email
        obj.breed=breed
        obj.quantity=quantity
        obj.number=number
        obj.save()
        return redirect('result')

    return render(request,"buy.html")

def result(request):
    return render(request,"result.html")

def cat(request):
    return render(request,"cat.html")

def dog(request):
    return render(request,"dog.html")

def catbuy(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        breed=request.POST.get('breed')
        quantity=request.POST.get('quantity')
        number=request.POST.get('number')

        obj=catdetails()
        obj.name=name
        obj.email=email
        obj.breed=breed
        obj.quantity=quantity
        obj.number=number
        obj.save()
        return redirect('result')
    return render(request,"catbuy.html")