from django.contrib import admin

# Register your models here.
from .models import UserToken, Gamebox, Flag
admin.site.register(UserToken)
admin.site.register(Gamebox)
admin.site.register(Flag)
