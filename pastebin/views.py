from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime
from django import template

from django.shortcuts import render,get_object_or_404
from pastebin.forms import input,Authentic
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from pastebin.models import paste
from datetime import datetime





def main_page(request):
    form=input()
    if request.method=="POST":
        form=input(request.POST)

        if form.is_valid():
            form.save()
            var1=request.POST.get("url")

            var = paste.objects.get(pk = var1)
            return render(request,"pastebin/ss.html",{"form":form,"var":var,"var1":var1 }) 
            
        else:
            print("error")    
    return render(request,"pastebin/paste.html",{"form":form }) 