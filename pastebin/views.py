from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime
from django import template

from django.shortcuts import render,get_object_or_404
from pastebin.forms import input,Authentic,input_logged_in
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from pastebin.models import paste,paste_logged_in
from datetime import datetime





def main_page(request):
    form=input()
    if request.method=="POST":
        form=input(request.POST)
        print(form)

        if form.is_valid():
            latest_model=form.save()
            var3=latest_model.url
            return render(request,"pastebin/ss.html",{"form":form,"var3":var3 }) 
            
        else:
            print("error")    
    return render(request,"pastebin/paste.html",{"form":form }) 

def content_fetch(request,url_no):
    content_object=paste.objects.get(pk = url_no)
    return render(request,"pastebin/fetching_content.html",{"content_object":content_object }) 


def user_signup(request):
    registered = False
    
    if request.method=="POST":
     auth=Authentic(request.POST )

     if auth.is_valid():
         auth=auth.save(commit=False)
         auth.set_password(auth.password)   
         #hashing the password
         auth.save()
         registered=True


     else :
         print("error")
    else:
        auth=Authentic()     
    return render(request,"pastebin/signup.html",{"auth":auth,"registered":registered })        


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)


        if user:
            login(request,user)
            return HttpResponseRedirect(reverse("pastebin:main_loggedin_page",))
        else:
            return HttpResponse("invalid username and password")
    else :
        return render(request,"pastebin/login.html",{})
@login_required
def main_loggedin_page(request):
   # username = None
    username = request.user.username
    # if request.user.is_authenticated():
    print(username)
    # print(username)
    form=input_logged_in()
    if request.method=="POST":
        form=input_logged_in(request.POST)
     #   print(form)
        obj=form.save(commit=False)
        obj.owner=username
      #  print(obj)


        if form.is_valid():
          #  latest_model1= form.save(commit=False)
            latest_model= form.save()
            var3=latest_model.url
            return render(request,"pastebin/ss_logged_in.html",{"form":form,"var3":var3,"username":username}) 
            
        else:
            print("error")    
    return render(request,"pastebin/paste_loggedin.html",{"form":form, }) 

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("pastebin:main_page",))