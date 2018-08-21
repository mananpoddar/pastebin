from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class paste(models.Model):
    content = models.TextField(max_length=1000000)
    url = models.AutoField(primary_key=True)
class paste_logged_in(models.Model):
    content = models.TextField(max_length=1000000)
    url = models.AutoField(primary_key=True)
    owner=models.ForeignKey(User,on_delete=models.PROTECT,default=1)