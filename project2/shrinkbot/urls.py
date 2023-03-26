from django.urls import path
from . import views
from members import views as members_views

urlpatterns = [
    path('', members_views.login, name='login'),
    path('<str:room>/', views.room, name='room'),
    # path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]