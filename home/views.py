from pyexpat.errors import messages
from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime


# Create your views here.
def index(request):

    return render(request,'index.html')
    #return HttpResponse("this is home page")


#def home(request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")    


def about(request):
    return render(request,'about.html')
    # return HttpResponse("this about page")

def services(request):
    return render(request,'services.html')
 # return HttpResponse("this about page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def pharamaandbiotech(request):
    return render(request,'pab.html')
    # return HttpResponse("this pharama and biotech")

def HospitalandHealthcare(request):
    return render(request,'ham.html')
    # return HttpResponse("Hospital and Health care")
    

 