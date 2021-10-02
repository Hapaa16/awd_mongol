from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Gamebox, Flag, UserToken
import secrets
from django.contrib.auth.decorators import user_passes_test
from ssh_handle import ssh_handler
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
    users = User.objects.all
    context = {'users': users}
    if request.method == "POST":
        game_box_name = request.POST.get('boxname')
        box_description = request.POST.get('description')
        box_ip = request.POST.get('ip')
        box_ssh_user = request.POST.get('sshname')
        box_ssh_pw = request.POST.get('sshpw')
        box_ssh_port =request.POST.get('port')
        team_id = request.POST.get('team')
        team = User.objects.all().filter(id=team_id)
        if not team[0].is_superuser:
            print(team)
            box_creation = Gamebox(box_name=game_box_name, ip=box_ip, ssh_user=box_ssh_user, ssh_password=box_ssh_user, ssh_port=box_ssh_port, description=box_description, user=team[0])
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
    all_boxes = Gamebox.objects.all()
    flag = Flag.objects.all()
    command = "echo '"+ flag[1].flags+"' > /flag"
    for box in all_boxes:
        ssh_handler(box.ip, box.ssh_user, box.ssh_password, command, box.ssh_port)
        print(box.id)  
    print('GAME STARTED !!!')
    return redirect('flag_uusgelt')
def prepare_page(request):
    context={}
    return render(request, 'game_prepare.html', context)