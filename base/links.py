from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path('register/',views.registeruser,name="register"),
    path('',views.home,name="home"),
    path('room/<int:pk>/',views.room,name="room"),
    path('create-room/',views.createroom,name="createroom"),
    path('update-room/<str:pk>/',views.updateroom,name="updateroom"),
    path('delete-room/<str:pk>/',views.deleteroom,name="deleteroom"),
    path('delete-message/<str:pk>/',views.deletemessage,name="deletemessage"),
    path('user-profile/<str:pk>/',views.userProfile,name="userProfile")



]