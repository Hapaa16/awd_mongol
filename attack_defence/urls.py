"""attack_defence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import static
from django.urls import path, include

from main.views import index, register, logout_page
from admin_side.views import index as index_admin, Gamebox_page, Flag_page, flag_generate, game_start, prepare_page
urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('logout', logout_page),
    path('god/', index_admin, name='index_admin'),
    path('god/gamebox/', Gamebox_page, name='gamebox'),
    path('god/register/', register, name='bag_uusgelt'),
    path('god/prepare/', prepare_page, name='prepare'),
    path('god/flag', Flag_page, name='flag_uusgelt'),
    path('god/flag/flaggen', flag_generate, name='flag_generate'),
    path('god/flag/gamestart', game_start, name='gamestart'),

]