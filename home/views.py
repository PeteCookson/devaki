from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, render
from .models import SubscribedUser
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def subscribe_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)

        if not first_name or not last_name or not email:
            messages.error(request, "You must provide a valid first name, last name, and email to subscribe to the Newsletter")
            return redirect("/")

        if SubscribedUser.objects.filter(email=email).exists():
            messages.error(request, f"The email address {email} has already subscribed to our newsletter.")
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

        # Send welcome email
        subject = 'Welcome to our Newsletter!'
        html_message = render_to_string('home/welcome_email.html', {'first_name': first_name})
        plain_message = strip_tags(html_message)
        from_email = 'pgcookson@gmail.com'  # Replace with your email address
        to_email = email

        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

        messages.success(request, f'The email address {email} was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))

    return redirect("/")

def home(request):
    return render(request, 'home/index.html')
