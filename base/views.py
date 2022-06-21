from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm


# rooms = [
  
# {'id': 1, 'name':'let us learn python!'},
# {'id': 2, 'name':'let us learn HTML!'},
# {'id': 3, 'name':'let us learn JavaScript!'},

# ]



def home(request):
    rooms=Room.objects.all()

    return render(request,'base/home.html',{'rooms':rooms})

def room(request,pk):
    room=Room.objects.get(id=pk)
    context={'room':room}        

    return render(request,'base/room.html',context)  

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
    if request.method== 'POST':
     form= RoomForm(request.POST,instance=room)
     if form.is_valid():
        form.save()
        return redirect('home')   

    context={'form':form}
    return render(request,'base/room_form.html',context) 

def deleteroom(request,pk):
     room=Room.objects.get(id=pk)
     if request.method== 'POST':
        room.delete()
        return redirect('home')


     return render(request,'base/delete.html',{'obj':room})

# Create your views here.
