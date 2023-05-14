"""
URL configuration for Access project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from .views import F_PASSWORD, HOME, LOGIN,REGISTRATION, logOut
from django.conf.urls.static import static
from Access import settings

urlpatterns = [
    path('',LOGIN, name="login_page"),
    path('registration/',REGISTRATION, name="registration_page"),
    path('forgot-password/',F_PASSWORD, name="forgot_password"),
    path('logout/',logOut,name="logout"),
    path('home/',HOME, name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
