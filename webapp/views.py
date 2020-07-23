from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import *
from .models import *


def homeView(request):
    form=Contactform()
    return render(request,'home.html',{'form':form})

def contactView(request):
    form=Contactform(request.POST)
    if form.is_valid():
        fname=form.cleaned_data['fname']
        femail=form.cleaned_data['femail']
        fmsg=form.cleaned_data['fmessage']
        s= ContactMsg(contact_name=fname,contact_email=femail,contact_msg=fmsg)
        s.save()
    return redirect('/')