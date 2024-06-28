from django.shortcuts import render,redirect

from .forms import ContactMessageForm

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

def price(request):
    return render (request,'base/price.html')



def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Ensure 'success' is a valid URL name in your URLs config
        else:
            print(form.errors)
    else:
        form = ContactMessageForm()

    return render(request, 'base/contact.html', {'form': form})
