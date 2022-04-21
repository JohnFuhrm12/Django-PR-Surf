"""Surf_App URL Configuration

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
from django.contrib import admin
from django.urls import path
from surf_report import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from users.models import CustomAuthForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('forecasts', views.forecasts, name='forecasts'),
    path('rincón', views.rincon, name='rincon'),
    path('isabela', views.isabela, name='isabela'),
    path('aguadilla', views.aguadilla, name='aguadilla'),
    path('register', user_views.register, name='register'),
    path('favorites', user_views.favorites, name='favorites'),
    path('login', auth_views.LoginView.as_view(authentication_form=CustomAuthForm, template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('fav/<int:id>/', views.favorite_add, name='favorite_add'),
]
