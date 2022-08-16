from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
from os import listdir
from django.core.paginator import Paginator


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    # files_list = listdir(path=r'C:\Users\olesy\PycharmProjects\Django homework\dj-homeworks\first-project\first_project')
    # return HttpResponse(files_list)

    context = {
        'files_list': listdir(path=r'C:\Users\olesy\PycharmProjects\Django homework\dj-homeworks\first-project\first_project')
    }

    return render(request, 'app/workdir.html', context)


def summ(request, a, b):
    result = a + b
    return HttpResponse(f'Sum is {result}')


CONTENT = [str(i) for i in range(10000)]


def pagi(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'app/pagi.html', context)