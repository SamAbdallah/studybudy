from django.http import JsonResponse
from django.urls import path
from . import views1

urlpatterns=[
    path('',views1.getroutes),
    path('rooms/',views1.allrooms),
    path('rooms/<str:pk>',views1.oneroom)


]