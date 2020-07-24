from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import auth
from .forms import *
from .models import *

def homeView(request):
    contactform=Contactform()
    loginform=Loginform()
    return render(request,'home.html',{'contactform':contactform,'loginform':loginform})

def contactView(request):
    form=Contactform(request.POST)
    if form.is_valid():
        fname=form.cleaned_data['fname']
        femail=form.cleaned_data['femail']
        fmsg=form.cleaned_data['fmessage']
        s= ContactMsg(contact_name=fname,contact_email=femail,contact_msg=fmsg)
        s.save()
    return redirect('/')

def loginview(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect("/")
    else:
        # Show an error page
        return redirect("/")