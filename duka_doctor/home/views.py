from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request): 
    emergencysection = EmergencySection.objects.all().order_by('-id')[0:4]
    departments = Departments.objects.all().order_by('-id')[0:6]
    why_choose = Why_Choose.objects.all().order_by('-id')[0:3]
    services = Services.objects.all().order_by('-id')[0:6]
    setting = Setting.objects.all().order_by('-id')[0:1]
    gallery = Gallery.objects.all().order_by('-id')[0:30]
    doctor = Doctor.objects.all().order_by('-id')[0:4]
    slider = Slider.objects.all().order_by('-id')[0:6]
    about = About.objects.all().order_by('-id')[0:1]
    usp = Usp.objects.all().order_by('-id')[0:4]
    faq = FAQ.objects.all().order_by('-id')[0:8]



    context={
        'emergencysection':emergencysection,
        'departments':departments,
        'why_choose':why_choose,
        'services':services,
        'setting':setting,
        'gallery':gallery,
        'doctor':doctor,
        'slider':slider,
        'about':about,
        'usp':usp,
        'faq':faq,


    }


    return render(request,'home.html',context)



def APPOINTMENT_THANKYOU(request):
    return render(request, 'appointment_thanks.html')