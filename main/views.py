from admin_side.models import UserToken
from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import secrets
# Create your views here.
def index(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                UserToken.objects.create(user=user, token=str(secrets.token_hex(16)))
                login(request, user)
                print('noError ?')
                return redirect('index')
            except:
                print(user.usertoken.token + 'aasdasd')
                login(request, user)
                return redirect('index')
        else:
            messages.info(request, 'Username or Password Buruu bn')
            return redirect('index')
        # if form.is_valid():
        #     user = form.get_user()
        #     login(request, user)
        #     return redirect('index')
    context = {'form': form}
    return render(request, 'index.html', context)
def logout_page(request):
    logout(request)
    return redirect('index')
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('index')
    context = {'form': form}
    return render(request, 'test_register.html', context)

