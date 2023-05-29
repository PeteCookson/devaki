from django.shortcuts import render

def about(request):
    # Your view logic here
    return render(request, 'about/about.html')
