import random
from django.shortcuts import render

# Create your views here.

def main(request):

    return render(request,"main.html")

def password_generator(request):
    context = {}
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    if request.method == "POST":
        letter = request.POST.get("pass_letter")
        number = request.POST.get("pass_number")
        symbol = request.POST.get("pass_symbol")

        password = ""
        for a in range(1, int(letter)+1):
            password = password+random.choice(letters)
            print(password)

        for b in range(1, int(number)+1):
            password = password+random.choice(numbers)
            print(password)


        for c in range(1,int(symbol)+1):
            password = password+random.choice(symbols)
            print(password)


        random_password = ""

        for d in range(1, len(password)):
            random_password_generator = random.choice(password)
            random_password += random_password_generator 
        message = f" your password is: {random_password}" 
        context ["password"] = random_password
        print(message)


        return render(request,"password_generator.html",context)

    return render(request,"password_generator.html",context)