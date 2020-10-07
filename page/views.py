from django.shortcuts import render
from .models import *
from blog.models import Menuitem
from .forms import *

def info_page(request):
    menu = Menuitem.objects.all()
    return render(request, 'page/info.html', context={'menu':menu})

def tehpris_page(request):
    menu = Menuitem.objects.all()
    return render(request, 'page/tehpris.html', context={'menu':menu})

def company_page(request):
    menu = Menuitem.objects.all()
    return render(request, 'page/company.html', context={'menu':menu})

def aviable_powers_page(request):
    menu = Menuitem.objects.all()
    return render(request, 'page/aviable-powers.html', context={'menu':menu})

def vacancy_page(request):
    vacancy = Vacancy.objects.all()
    menu = Menuitem.objects.all()

    return render(request, 'page/vacancy.html', context={'menu':menu, 'vacancy':vacancy})

def anketa(request):
    menu = Menuitem.objects.all()
    form = AnketaForm()

    return render(request, 'page/vacancy-anketa.html', {'form': form, 'menu':menu})

def regular_page(request, slug):
    page = Page.objects.get(slug__iexact=slug)
    menu = Menuitem.objects.all()
    return render(request, 'page/page_regular.html', context={'page':page, 'menu':menu})
