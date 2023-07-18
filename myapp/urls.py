
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('mainproperty', mainproperty, name='mainproperty'),
    path('services', services, name='services'),
    path('contactus', contactus, name='contactus'),
    path('contactagent', contactagent, name='contactagent'),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('property', property, name='property'),
    path('property2', property2, name='property2'),
    path('property3', property3, name='property3'),
    path('property4', property4, name='property4'),
    path('property5', property5, name='property5'),
    path('search',search, name='search'),
    path('registeruser',registeruser,name='registeruser'),
    path('logout',logout,name='logout'),

]
