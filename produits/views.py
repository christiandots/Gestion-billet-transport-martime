from django.shortcuts import render, HttpResponse

def index(request, *args, **kwargs):
    return render(request, 'index.html', {})

# Create your views here.
