from django.shortcuts import render
from .models import *

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from time import time
import datetime


def main(request):
    posts = Post.objects.filter().exclude(category=12)
    paginator = Paginator(posts, 10)
    postwoff = Wateroff.objects.all()
    woff_paginator = Paginator(postwoff, 5)
    pagewoff = woff_paginator.get_page(1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    menu = Menuitem.objects.all()
    now = datetime.datetime.now()
    return render(request, 'blog/base.html', context={'pnhvs': pagewoff, 'posts': page, 'menu':menu, 'now':now})

def post_single(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    menu = Menuitem.objects.all()

    return render(request, 'blog/post_single.html', context={'post':post, 'menu':menu })

def woff_single(request, id):
    post = Wateroff.objects.get(id__exact=id)
    menu = Menuitem.objects.all()

    return render(request, 'blog/woff_single.html', context={'post':post, 'menu':menu })

def uk_info(request):
    menu = Menuitem.objects.all()
    post = Post.objects.filter(category=12)

    return render(request, 'blog/uk-info.html', context={'post':post, 'menu':menu })

def uk_info_single(request, slug):
    menu = Menuitem.objects.all()
    post = Post.objects.get(slug__iexact=slug)

    return render(request, 'blog/post_single.html', context={'post':post, 'menu':menu })

def news(request):
    posts = Post.objects.filter().exclude(category=12)
    menu = Menuitem.objects.all()
    paginator = Paginator(posts, 12)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'blog/news.html', context={'posts':page, 'menu':menu })
