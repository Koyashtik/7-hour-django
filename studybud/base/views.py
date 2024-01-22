from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

# rooms = [
#     {'id':1, 'name':'lets learn python '},
#     {'id':2, 'name':'is it unity?'},
#     {'id':3, 'name':'we will learn computer vision'},
# ]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})

def room(request, pk):
    room= Room.objects.get(id=pk)
    context= {'room':room}
    
    return render(request,'room.html', context)


def createRoom(request):
    context= {}
    return render(request, 'room_form.html', context)