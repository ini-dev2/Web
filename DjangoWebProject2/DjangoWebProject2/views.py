from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

def home(request):
    """Главная страница сайта"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Главная',
            'year': datetime.now().year,
        }
    )

def login(request):
    return render(request, 'app/login.html')

def links(request):
    """Страница с полезными ссылками и ресурсами"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title': 'Полезные ресурсы',
            'year': datetime.now().year,
        }
    )

def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Конктакты',
            'year': datetime.now().year,
        }
    )

def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'О нас',
            'year': datetime.now().year,
        }
    )


    
    return render(request, 'app/login.html', {'form': form})

def registration(request):
    """Страница регистрации нового пользователя"""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()
            return redirect('login')
    else:
        regform = UserCreationForm()

    return render(
        request,
        'app/registration.html',  # Используем шаблон для страницы регистрации
        {
            'regform': regform,
            'year': datetime.now().year,
            'is_registration_page': True  # Передаем флаг, чтобы скрыть меню
        }
    )
