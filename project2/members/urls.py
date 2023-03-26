# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.login_user, name='login'),
# ]




# //devproject/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    # path('signout/',views.signout, name='signout'),
    path('register',views.register, name='register'),
    # path('profile/',views.profile, name='profile'),
]