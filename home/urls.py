from django.urls import path
from .views import *

urlpatterns = [
    path("/", home , name='home'),
    path( "/about-us", about_us , name='about')
]