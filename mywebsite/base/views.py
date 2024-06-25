from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'base/home.html')

def project(request):
	return render(request, 'base/project.html')

def team(request):
	return render(request, 'base/team.html')

def calender(request):
	return render(request, 'base/calender.html')
def basss(request):
	return render(request, 'base/basss.html')
