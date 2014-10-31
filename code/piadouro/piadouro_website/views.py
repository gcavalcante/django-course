from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

#Importing piado_website models
from piadouro_website.models import Piado

# Create your views here.
def home(request):
  return render_to_response("piadouro_website/home.html", 
                  { "piados" : Piado.objects.all() })

