from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('room/<int:pk>/',views.room,name="room"),
    path('create-room/',views.createroom,name="createroom"),
    path('update-room/<str:pk>/',views.updateroom,name="updateroom"),
    path('delete-room/<str:pk>/',views.deleteroom,name="deleteroom")


]