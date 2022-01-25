import os
from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, 'home.html', context)


def time_view(request):
    time_now = datetime.now().time()
    msg = f'<h3>Текущее время в Красноярске:</h3> \n<h1>{time_now.strftime("%H:%M:%S")}</h1>' \
          f'<a href="{reverse("home")}">Вернуться на главную </a>' \
          f'<script type="text/javascript">setTimeout(()=>location.reload(),1000)</script>'
    return HttpResponse(msg)



def workdir_view(request):
    files = '<br/>'.join(os.listdir(path='.'))
    msg = f'Содержимое рабочей директории:<br/> {files}' \
          f'<a href="{reverse("home")}">Вернуться на главную </a>' \
          f'<script type="text/javascript">setTimeout(()=>location.reload(),1000)</script>'
    return HttpResponse(msg)