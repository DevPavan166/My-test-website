from django.shortcuts import render
from django.core.mail import send_mail 
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.

def home(request):
    
    
    if request.method == 'POST':
        emails = request.POST['email']
        messages = request.POST['massage']

        send_mail(
        'Contct from alpha (Home page)> '+ emails, 
        messages, 
        settings.EMAIL_HOST_USER,
        ['pavanpatel312604@gmail.com'],
        fail_silently=False,
        )
        return redirect('/thanks/')
        
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        emails = request.POST['email']
        names = request.POST['name']
        phones = request.POST['phone']

        send_mail(
        'Contct from alpha (Contact page) > '+ emails, 
        names + ' > ' +phones, 
        settings.EMAIL_HOST_USER,
        ['pavanpatel312604@gmail.com'],
        fail_silently=False,
        )
        return redirect('/thanks/')
        
    return render(request, 'demo-medical-contact.html')

def about(request):
    if request.method == 'POST':
        emails = request.POST['email']
        names = request.POST['name']
        phones = request.POST['phone']

        send_mail(
        'Contct from alpha (about page) > '+ emails, 
        names + ' > ' +phones, 
        settings.EMAIL_HOST_USER,
        ['pavanpatel312604@gmail.com'],
        fail_silently=False,
        )
        return redirect('/thanks/')
    return render(request, 'demo-gym-about-us.html')

def card(request):
    
    return render(request, 'alpha-card.html')

def airmed(request):
    return render(request, 'airmed.html')

def sun(request):
    return render(request, 'sun-studio.html')

def privacy (request):
    return render(request, 'privacy-policy.html')    

def thanks (request):
    return render(request, 'thanks.html')

def error_404_view(request, exception):
    return render(request, '404.html')

