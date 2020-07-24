from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home'),
    path('contact', contactView, name='contact'),
    path('login', loginview, name='login')
]