from django.shortcuts import render

def family_room(request):
    return render(request, 'family_room/family_room.html')
