"""calc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index),
    path('golden-ratio', views.met_gold),
    path('half-division', views.met_pol_pod),
    path('fibonacci', views.met_fib),
    path('sven', views.met_svenn),
    path('konfiguration', views.met_konfig),
    path('deform', views.met_deform),
    path('naprjamkiv', views.met_nap),
    path('random', views.met_ran,),
]
