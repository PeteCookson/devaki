from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe/', views.subscribe_user, name='subscribe_user'),
]