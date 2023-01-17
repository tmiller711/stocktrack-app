from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_func, logout as logout_func

from .forms import LoginForm, RegisterForm

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.data.get('email')
            password = form.data.get('password')

            account = authenticate(request, email=email, password=password)
            if account is not None:
                login_func(request, account)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', context={'form': form})

def register(request):
    user = request.user
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            return redirect("/login")
    else:
        form = RegisterForm()

    return render(request, "register.html", context={"form": form})

def logout(request):
    logout_func(request)
    return redirect('/')