from django.urls import path
from . import views
from members import views as members_views

urlpatterns = [
    path('<str:username>/profile/', views.profile,name='profile'),
    path('<str:username>/profile/chatroom', views.chatroom,name='chatroom'),
    path('getQueries/<str:username>/', views.getQueries, name='getQueries'),
    path('send', views.send, name='send'),
]