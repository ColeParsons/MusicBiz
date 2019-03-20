from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf.urls import url
from .models import Artist

def index(request):
    all_Artists = Artist.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        
        'all_Artists' : all_Artists,
        
    }
    return HttpResponse(template.render(context, request))
    
def detail(request, Stage_Name): 
    
    return HttpResponse("<h1>List of artists" + str(Stage_Name)+ "</h1>")

