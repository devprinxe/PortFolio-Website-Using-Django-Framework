from django.shortcuts import render
from .models import *
  
# Create your views here. 
def home(request): 
      
    # render function takes argument  - request 
    # and return HTML as response 
    information = PersonalInformation.objects.all()
    social = SocialMediaLinks.objects.all()
    webinfo = Website.objects.all()
    review = Testimonial.objects.all()
    cv = Resume.objects.all()
    client = Fact.objects.all()
    work = Portfolio.objects.all()
    skills = Skill.objects.all()
    return render(request, "index.html", {'social': social,'information': information, 'webinfo':webinfo, 'review': review, 'cv': cv, 'client': client, 'work': work, 'skills': skills}) 