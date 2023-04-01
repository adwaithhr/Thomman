
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('logout',views.logout_view, name='logout'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register')
]