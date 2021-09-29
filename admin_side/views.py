from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Gamebox, Flag, UserToken
import secrets
# Create your views here.
from django.contrib.auth.decorators import user_passes_test
def index(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                print(request.POST['username'])
                return redirect('index_admin')
            else:
                messages.info(request, 'You are not admin GTFO BITCH!')
                return redirect('index_admin')
        else:
            messages.info(request, 'Username or Password Buruu bn')
            return redirect('index')
    context = {'form': form}
    return render(request, 'admin_index.html', context)
@user_passes_test(lambda u: u.is_superuser)
def Gamebox_page(request):
    context = {}
    if request.method == "POST":
        game_box_name = request.POST.get('boxname')
        box_creation = Gamebox(box_name=game_box_name)
        box_creation.save()
    return render(request, 'gamebox.html', context)
@user_passes_test(lambda u: u.is_superuser)
def Flag_page(request):
    return render(request, "flag.html")
def flag_generate(request):
    flag_prefix = "nabactf{"
    flag_suffix = "}"
    first_box =  Gamebox.objects.first()
    for round in range(3):
        flag = flag_prefix+str(secrets.token_hex(16))+flag_suffix
        flag_to_db = Flag(flags=flag)
        flag_to_db.box = first_box
        flag_to_db.save()
    print('flag generate')
    return redirect('flag_uusgelt')
def game_start(request):
    print('GAME STARTED !!!')
    return redirect('flag_uusgelt')