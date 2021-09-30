from django.shortcuts import redirect, render

# Create your views here.

def main(request):

    return render(request,"main.html")

def password_generator(request):

    return render(request,"password_generator.html")