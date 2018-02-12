from django.shortcuts import render
from .forms import BronForm

def index(request):
    form = BronForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'main/home_page.html')
