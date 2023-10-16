
#Import necessary modules and models.
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, render
from .models import SubscribedUser

from django.core.mail import send_mail
from devaki.settings import EMAIL_HOST_USER

from django.template.loader import render_to_string
from django.utils.html import strip_tags

#Define the subscribe_user view function.
def subscribe_user(request):
    #Check if the request method is POST.
    if request.method == 'POST':
        # Get the form data from the request.
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)

        # Validate the form data and handle any errors.
        if not first_name or not last_name or not email:
            messages.error(request, "You must provide a valid first name, last name, and email to subscribe to the Newsletter")
            return redirect("/")

        # Check if the email is already subscribed and handle the case.
        if SubscribedUser.objects.filter(email=email).exists():
            messages.error(request, f"The email address {email} has already subscribed to our newsletter.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        # Validate the email address and handle any validation errors.
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        # Create a new SubscribedUser instance and save it to the database.
        subscribe_model_instance = SubscribedUser()
        subscribe_model_instance.first_name = first_name
        subscribe_model_instance.last_name = last_name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()

        # Send a welcome email to the subscriber.
        # subject = 'Welcome to our Newsletter!'
        # html_message = render_to_string('welcome_email.html', {'first_name': first_name})
        # plain_message = strip_tags(html_message)
        # from_email = EMAIL_HOST_USER
        # to_email = email

        # print("Before sending email")
        # send_mail(subject, plain_message, from_email, [to_email], fail_silently=True, html_message=html_message)
        # print("After sending email")

        # Display a success message and redirect back to the previous page.
        messages.success(request, f'The email address {email} was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))

    #If the request method is not POST, redirect to the home page.
    return redirect("/")

def home(request):
    return render(request, 'home/index.html')
