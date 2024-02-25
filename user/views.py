from django.views.generic import *
from .models import Enquire
from django.urls import reverse
from django.http import HttpResponse
from properties.models import Property
from django.shortcuts import render
from django.template.loader import get_template 

# Create your views here.

def homepageView(request):
    cData = Property.objects.filter(projStatus='Completed').count()
    oData = Property.objects.filter(projStatus='Ongoing').count()
    return render(request, "home_page.html", {'completedCount': cData,  'onGoingCount': oData})

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(CreateView):
    template_name = 'contact.html'
    model = Enquire
    fields = '__all__'   
    success_url = "contact"

class ScopeView(TemplateView):
    template_name = 'scope.html'

class HowItWorks(TemplateView):
    template_name = 'how_it_works.html'


   

