from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.

def home(request):
	return render(request, 'base/home.html')

def project(request):
	return render(request, 'base/project.html')

def team(request):
	return render(request, 'base/team.html')

def calender(request):
	return render(request, 'base/calender.html')


def get_started(request):
    return render(request, 'base/team.html')

def success(request):
    return render (request,'base/success.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Here you can do further processing like sending emails, saving to database, etc.
            # For now, let's redirect to a success page
            return redirect('success')  # Assuming 'success' is the name of your success URL pattern
    else:
        form = ContactForm()
    
    return render(request, 'base/contact.html', {'form': form})

