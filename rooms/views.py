from django.shortcuts import render

def show_rooms(request):
    return render(request, 'rooms/show_rooms.html')
