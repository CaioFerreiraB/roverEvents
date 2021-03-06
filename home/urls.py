"""cultivese URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('envolvidos/', views.envolvidos, name='envolvidos'),
    path('checkin/', views.checkin, name='checkin'),
    path('pre_checkin/', views.pre_checkin, name='pre_checkin'),
    path('checkin/submit/', views.submit, name='submit'),
    path('pdf_view/<int:boletim_numero>/', views.pdf_view, name='pdf_view'),
]
