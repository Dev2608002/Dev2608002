from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session



def login(request):
    if request.session.has_key('is_login'):
        return redirect('home')

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        count = User.objects.filter(email=email,password=password).count()
        if count>0:
            request.session['is_login']=True
            return redirect('home.html')
        else:
            messages.error(request,"wrong id and password")
            return redirect('login')
            #return HttpResponse("wrong id and password")

    return render(request,'home.html')


def signup(request):
    return render(request,'signup.html')


def registeruser(request):
    if request.POST:
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        obj=User(username=username,email=email,password=password)
        obj.save()
        messages.success(request,"Registraton Done")
        return redirect('login')


    return HttpResponse("data insert done")


def property(request):
    return render(request,'property.html')


def property2(request):
    return render(request,'property2.html')


def property3(request):
    return render(request,'property3.html')


def property4(request):
    return render(request,'property4.html')


def property5(request):
    return render(request,'property5.html')


def home(request):
    if request.session.has_key('is_login'):
        return render(request,'home.html')
    else:
        return redirect('login')


def mainproperty(request):
        data = Mainproperty.objects.all()
        return render(request,'mainproperty.html',{'data':data})



def search(request):
    return render(request,'mainproperty.html')


def header(request):
    return render(request,'header.html')


def services(request):
    if request.POST:
        FullName = request.POST['FullName']
        email = request.POST['email']
        City = request.POST['City']
        message = request.POST['message']
        ApartmentSize = request.POST['ApartmentSize']
        obj =Service(FullName=FullName,email=email,City=City,message=message,ApartmentSize=ApartmentSize)
        obj.save()
        return HttpResponse("Enquiry sent. You will Recive Enquiry by admin within 2 days")

    return render(request, 'services.html')

def footer(request):
    return render(request,'footer.html')

def contactus(request):
    if request.POST:
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        obj = Contactus(Firstname=Firstname,Lastname=Lastname, email=email, subject=subject,message=message)
        obj.save()
        messages.success(request, "Message sent")
    return render(request, 'contactus.html')

def contactagent(request):
    return render(request,'contactagent.html')

def logout(request):
    return render(request,'login.html')