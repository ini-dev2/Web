from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('links/', views.links, name='links'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('registration/', views.registration, name='registration'),
]