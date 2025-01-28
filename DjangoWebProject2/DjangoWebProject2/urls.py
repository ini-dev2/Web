from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='app/login.html'), name='home'),
    path('index/', views.home, name='index'),
    path('links/', views.links, name='links'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('registration/', views.registration, name='registration'),
]