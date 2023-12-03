from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from task.forms import taskForm
from task.models import taskmaster
from django.contrib.auth import authenticate, logout, login
import datetime


# Create your views here.
def home (request):
    time = 0
    if request.user.is_authenticated:
        user_id = request.user
        if str(user_id) == 'workspace':
            id = taskmaster.objects.all()
        else:
            id = taskmaster.objects.filter(userid = user_id)
        today = datetime.date.today()
        weekday = today.day
    
        for i in id:
            d2 = i.date
            last = today-d2
            if last.days >= weekday:
                continue
            else:
                time = time + int(i.timetaken)
        
    
        hh = (time//60)
        mm = (time%60)
        ahh = int(time//60)//weekday
        amm = ((time//weekday)%60)

        return render(request, 'index.html',{'data':id, 'hh':hh, 'mm':mm, 'ahh':ahh, 'amm':amm})
    else:
        return redirect(login_view)

def task (request):
    if request.user.is_authenticated:
        today = datetime.date.today()
        
        user_id = request.user
        data = taskmaster.objects.filter(userid = user_id).filter(date=today)
        todaytime = 0
        for i in data:
            todaytime = todaytime + i.timetaken
        
        thh = todaytime//60
        tmm = todaytime%60
        if request.method == "POST":
            fm = taskForm(request.POST)
            if fm.is_valid():
                data = fm.cleaned_data
                taskdata = taskmaster(task =data['task'], enquiryNo = data['enquiryNo'], timetaken = data['timetaken'], comments = data['comments'], userid = user_id,)
                taskdata.save()
                return redirect(task)
        else:
            fm = taskForm()
            return render(request,'task.html',{'form':fm, 'data':data, 'thh':thh,'tmm':tmm})
    else:
        return redirect(login_view)

def report(request):
    if request.user.is_authenticated:
        return redirect(home)
    else:
        return redirect(login_view)


def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('user_name')
        pwd = request.POST.get('password')
        user = authenticate(username = uname, password = pwd)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view (request):
    logout(request)
    return redirect(login_view)