from django.shortcuts import render

def example(request):
    return render(request, 'example/example_page.html')
