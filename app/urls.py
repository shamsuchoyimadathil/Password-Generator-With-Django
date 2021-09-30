from django.urls import path 
from . import views

urlpatterns = [
    path("",views.main, name="main"),
    path("password-generator",views.password_generator, name="password_generator"),
]
