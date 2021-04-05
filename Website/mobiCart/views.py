from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, StreamingHttpResponse
#from . import models
from .models import Register, Validate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
# from mobiCart.VideoCapture import VideoCam
#from django.urls import reverse
# import csv
# import cv2
# import numpy as np
# import pandas as pd

# Create your views here.

name = ""
def homepage(request):

    return render(request, 'frontpage.html')


def airpods(request):
    return render(request, 'airpods.html')

#def airpodsHome(request):
#    return redirect(reverse('userhome'))


def cart(request):
    return render(request, 'cart.html')
'''def register(request):
    if request.method == 'POST':
        email = request.POST['emailadd']
        password = request.POST['password']
        with open('regdata.csv','a',newline='') as csvfile:
            wrt=csv.writer(csvfile)
            wrt.writerow(email)
            wrt.writerow(password)
            csvfile.close()

    return render(request, 'registerpage.html')

def login(request):
    if request.method=='POST':
        username=request.POST['userid']
        password1 = request.POST['pwd']
        with open('regdata.csv','r') as csvfile:
            red=csv.reader(csvfile)
            #col=next(red)
            i=1
            for row in red:
                if i%2!=0:
                    #print(list(username))
                    #print(list(password1))
                    if row==list(username):
                        flag=1
                    if row == list(password1):
                        flag=2
                i+=1
                print(row+1)
            csvfile.close()

    return render(request, 'Login.html')'''


def register(request):
    global name
    if request.method == 'POST':
        data = Validate(request.POST)
        username = data['emailadd']
        # data = Validate(username)

        if data.is_valid():
        #     data = request.POST

            password = data['password']
            name = data['firstname']
            hashed_password = make_password(password)
            #The next statement saves the details passed as parameters into the database
            new_user = User(username=username, password=hashed_password, first_name=name)
            new_user.save()
        #new_userprofile = UserProfile(user=new_user)
        return redirect('loginpage')
    else:
        return render(request,'registerpage.html')


def userlogin(request):
    if request.method=='POST':
        username1 = request.POST['userid']
        password = request.POST['pwd']
        # global name
        # name=username1
        user = authenticate(request, username=username1, password=password)
        if user is not None:
            login(request, user)
            return redirect('userhome')
        else:
            messages.error(request, "Please enter valid Login Credentials!!")
            return redirect('loginpage')

    else:
        return render(request, 'Login.html')


def userlogout(request):
    logout(request)
    return redirect('frontpage.html')


def userhome(request):
    if request.method=='POST':
        pass
    else:
        global name
        #The following statements fetch the name of the most recently registered user; needs correction to fetch name of user logged in recently
        name_list=name.split("@")
        str = "Welcome to mobiCart "+name_list[0] + " !!"
        # str=name
        return render(request, 'userfrontpage.html', {'msg': str})


# def gen_video(camera):
#
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#
#
# def showvideo(request):
#     try:
#         return StreamingHttpResponse(gen_video(VideoCam()), content_type='multipart/x-mixed-replace; boundary=frame')
#     except:
#         pass
#



