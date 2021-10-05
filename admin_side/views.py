from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Gamebox, Flag, UserToken, Game_settings, Rounds
import secrets
from django.contrib.auth.decorators import user_passes_test
from ssh_handle import ssh_handler
import datetime
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
    game_settings = Game_settings.objects.first()
    many_round = int(game_settings.all_round)
    for round in range(1, many_round+1):
        flag = flag_prefix+str(secrets.token_hex(16))+flag_suffix
        flag_to_db = Flag(flags=flag, box=first_box)
        flag_to_db.save()
        a_round = Rounds(round_dugaar=round, flags = flag_to_db)
        a_round.save()
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
    if request.method == "POST":
        ymd = request.POST.get('yearmonthday')
        hour_minute = request.POST.get('hourminute')
        b_year = int(ymd[0:4])
        b_month = int(ymd[5:7])
        b_day = int(ymd[8:10])
        b_hour = int(hour_minute[0:2])
        b_minute = int(hour_minute[3:])
        
        e_ymd = request.POST.get('endymd')
        e_hour_minute = request.POST.get('endhm')
        e_year = int(e_ymd[0:4])
        e_month = int(e_ymd[5:7])
        e_day = int(e_ymd[8:10])
        e_hour = int(e_hour_minute[0:2])
        e_minute = int(e_hour_minute[3:])
        diff_in_minutes = (e_day - b_day)*24*60+(e_hour - b_hour)*60 + (e_minute - b_minute)
        
        round_min = request.POST.get('round')
        round_min = int(round_min)
        all_rounds = diff_in_minutes / round_min
        all_rounds = round(all_rounds)
        save = Game_settings(all_round = all_rounds)
        save.save()

        print(all_rounds)
    return render(request, 'game_prepare.html', context)