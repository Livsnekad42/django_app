from django.shortcuts import render, redirect
from base.forms import RoomForm
from base.models import Room


def index(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, val):
    _room = Room.objects.get(id=val)
    context = {'room': _room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, val):
    _room = Room.objects.get(id=val)
    form = RoomForm(instance=_room)
    context = {'form': form}
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=_room)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html', context)


def destroyRoom(request, val):
    _room = Room.objects.get(id=val)
    form = RoomForm(instance=_room)
    if request.method == 'POST':
        form = RoomForm(request.POST)
        form.delete()
    context = {'form': form}
    return render(request, 'base/delete.html', context)
