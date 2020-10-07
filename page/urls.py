from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *



urlpatterns = [


    path('company/', company_page, name='page_company_url'),
    path('company/vacancy/', vacancy_page, name='page_vacancy_url'),
    path('company/vacancy/anketa/', anketa, name="anketa_url"),
    path('info/', info_page, name='page_info_url'),
    path('n-tehpris/', tehpris_page, name='page_tehpris_url'),
    path('n-tehpris/aviable-powers/', aviable_powers_page, name='page_aviable_powers_url'),
    path('<str:slug>', regular_page, name='reg_page_url'),


]
