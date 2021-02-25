from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contact, name='contactus'),
    path('about-us/', views.about, name= 'aboutus'),
    path('privacy-policy/', views.privacy, name= 'privacy-policy'),
    path('e-card/', views.card, name= 'alpha-card'),
    path('airmed/', views.airmed, name= 'airmed'),
    path('sun-studio/', views.sun, name= 'sun'),
    path('thanks/', views.thanks, name = 'thank you'),
]