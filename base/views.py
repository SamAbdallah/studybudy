from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room,topic
from .forms import RoomForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def loginPage (request):
    page='login'

    if request.user.is_authenticated:
        return redirect ('home') 

    if request.method== 'POST':
        username= request.POST.get('username').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'user does not exist')    

        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else :
            messages.error(request,'username and password does not exist')        
    
    context={'page':page}
    return render(request, 'base/login_register.html',context )


def logoutuser(request):
    logout(request)
    return redirect('home')

def registeruser(request):
    form=UserCreationForm() 
    if request.method=='POST':
        form=UserCreationForm(request.POST) #Pass the data#
        if form.is_valid():
            user=form.save(commit=False) #to acess the user right away to be able to clean data(lower case...)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration')    

    return render(request,'base/login_register.html',{'form':form})

def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    rooms=Room.objects.filter(


        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        
        
        )
    topicss=topic.objects.all()

    room_count=rooms.count()

    context={'rooms':rooms,'topicss':topicss,'room_count':room_count}

    return render(request,'base/home.html',context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room':room}        

    return render(request,'base/room.html',context)  

@login_required(login_url='login')
def createroom(request):
    form=RoomForm()
    if request.method== 'POST':
     form= RoomForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('home')   

    context={'form':form}
    return render(request,'base/room_form.html',context)     




def updateroom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed here!")

    if request.method== 'POST':
     form= RoomForm(request.POST,instance=room)
     if form.is_valid():
        form.save()
        return redirect('home')   

    context={'form':form}
    return render(request,'base/room_form.html',context) 


@login_required(login_url='login')
def deleteroom(request,pk):
    room=Room.objects.get(id=pk)
    if request.user != room.host:
     return HttpResponse("You are not allowed here!")
    if request.method== 'POST':
        room.delete()
        return redirect('home')


    return render(request,'base/delete.html',{'obj':room})

# Create your views here.
