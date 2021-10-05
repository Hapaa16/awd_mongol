from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    def __str__(self):
        return self.token
class Gamebox(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    box_name = models.CharField(max_length=100)
    ip = models.CharField(max_length=20, null=True)
    ssh_user = models.CharField(max_length=30, null=True)
    ssh_password = models.CharField(max_length=100, null=True)
    ssh_port = models.IntegerField(null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.box_name
class Flag(models.Model):
    flags = models.CharField(max_length=150)
    box = models.ForeignKey(Gamebox, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.flags

class Game_settings(models.Model):
    all_round = models.CharField(default=None, null=True, max_length=10)
    def __str__(self):
        return self.all_round
    
class Rounds(models.Model):
    round_dugaar = models.IntegerField(null=True)
    flags = ForeignKey(Flag, default=None, on_delete=models.CASCADE)
    
# Create your models here.
