from django.shortcuts import render

def home(request):
    # Your view logic here
    return render(request, 'home/index.html')