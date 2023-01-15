from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_func

from .forms import LoginForm

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.data.get('email')
            password = form.data.get('password')

            account = authenticate(request, email=email, password=password)
            if account is not None:
                login_func(request, account)
                print("success")
    else:
        form = LoginForm()
    return render(request, 'login.html', context={'form': form})

def register(request):
    pass