"""Theme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include
from app import views

# from app.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register_success/', views.register_success, name='register_ok'),
    path('user_active/<int:token>/', views.user_active, name='active'),
    path('login/', views.login_views, name='login'),
    path('verify_code/', views.verify_code, name='verify_code'),
    path('logout/', views.logout_views, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('instruction/', views.instruction, name='instruction'),
    path('work/', views.work, name='work'),
]
