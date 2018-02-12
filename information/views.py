from django.shortcuts import render

def inform(request):
    return render(request, 'information/inform.html')
