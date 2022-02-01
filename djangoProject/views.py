from django.shortcuts import render, redirect
from django.db.models import Q
from base.forms import RoomForm
from base.models import Room, Topic
from django.contrib.auth.models import User


def index(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(host__username=q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            raise ValueError("This user is not in database")
    context = {}
    return render(request, 'base/login_register.html', context)


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
    if request.method == 'POST':
        _room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': _room.name})
