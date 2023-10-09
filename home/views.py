from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SubscribedUser

def subscribe_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)

        if not first_name or not last_name or not email:
            messages.error(request, "You must provide a valid first name, last name, and email to subscribe to the Newsletter")
            return redirect("/")

        if SubscribedUser.objects.filter(email=email).exists():
            messages.error(request, f"{email} email address is already a subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUser()
        subscribe_model_instance.first_name = first_name
        subscribe_model_instance.last_name = last_name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))

    return redirect("/")

def home(request):
    return render(request, 'home/index.html')
