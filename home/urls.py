from django.urls import path
from .views import *

urlpatterns = [
    path("/", HomePage , name='home'),
    path( "/about-us", about_us , name='about'),
]