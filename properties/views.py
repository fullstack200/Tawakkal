from django.views.generic import *
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Property

def residentialMenuView(request):
    myData = Property.objects.filter(projectType='Residential',projStatus="Completed").values()
    template = loader.get_template('residential.html')
    context = {
        'rproperties': myData,
    }
    return HttpResponse(template.render(context, request))

def commercialMenuView(request):
    myData = Property.objects.filter(projectType='Commercial',projStatus="Completed").values()
    template = loader.get_template('commercial.html')
    context = {
        'cproperties': myData,
    }
    return HttpResponse(template.render(context, request))

def onGoingMenuView(request):
    myData = Property.objects.filter(projStatus='Ongoing').values()
    template = loader.get_template('ongoing.html')
    context = {
        'oproperties': myData,
    }
    return HttpResponse(template.render(context, request))

def detailView(request, id,):
    property = Property.objects.get(id=id)
    template = loader.get_template('project_info.html')
    context = {
        'property': property,
    }

    return HttpResponse(template.render(context, request))
