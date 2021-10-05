from django.contrib import admin

# Register your models here.
from .models import UserToken, Gamebox, Flag, Game_settings, Rounds
admin.site.register(UserToken)
admin.site.register(Gamebox)
admin.site.register(Flag)
admin.site.register(Game_settings)
admin.site.register(Rounds)
