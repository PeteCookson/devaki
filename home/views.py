from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import SubscribedUsers

def home(request):
    return render(request, 'home/index.html')