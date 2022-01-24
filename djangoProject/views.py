from django.shortcuts import render

from base.models import Room






def index(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, val):
    room = Room.objects.get(id=val)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)
