"""MP URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from app import views
from app.views import join

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', include('app.urls')),
    path('index2', views.index2),
    path('index3', views.index3),
    path('card', views.card),
    path('card2', views.card2),
    path('sign', views.sign),
    path('join/', views.join),
    path('login/', views.login),
]
