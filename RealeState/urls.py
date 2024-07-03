"""
URL configuration for RealeState project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from RealeState import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('mainproperty/', views.mainproperty, name='mainproperty'),
    path('services/', views.services, name='services'),
    path('contactus/', views.contactus, name='contactus'),
    path('contactagent/', views.contactagent, name='contactagent'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('property/',views.property, name='property'),
    path('property2/', views.property2, name='property2'),
    path('property3/', views.property3, name='property3'),
    path('property4/', views.property4, name='property4'),
    path('property5/', views.property5, name='property5'),
    path('search/',views.search, name='search'),
    path('registeruser/',views.registeruser,name='registeruser'),
    path('Calc/',views.Calc,name='Calc'),
    path('logout/',views.logout,name='logout'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
