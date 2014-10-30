from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def home(request):
  return render_to_response("piadouro_website/home.html", 
                  {"hello": "Beep, Beep, Beeep! I'm alive!"})

