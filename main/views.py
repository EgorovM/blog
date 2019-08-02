from django.shortcuts import render

def index(request):

    return render(request, 'main/index.html');

def section(request):

    return render(request, 'main/section.html');
