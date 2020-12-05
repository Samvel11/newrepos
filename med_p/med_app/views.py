from django.shortcuts import render, redirect

# Create your views here.

def home(request):
	return render(request, "med_app/welcome_base.html")

def about(request):
	return render(request, "med_app/about.html")	
