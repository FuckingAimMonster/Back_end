from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True, verbose_name='아이디')
    password = models.CharField(max_length=30, verbose_name='비밀번호')
    nickname = models.CharField(max_length=20, unique=True, verbose_name='닉네임')
    mousedpi = models.CharField(max_length=20, null=True, blank=True, verbose_name="DPI")
    gamedpi = models.CharField(max_length=20, null=True, blank=True, verbose_name="인게임 감도")
    currentdpi = models.CharField(max_length=20, null=True, blank=True, verbose_name="현재 감도")

class SignIn(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name='아이디')
    password = models.CharField(max_length=30, verbose_name='비밀번호')

class CheckId(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name='아이디')