from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login/")
def menu(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('description')
        receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description
        )
        return redirect('menu')
    
    queryset = receipe.objects.all()
    context = {'receipe' : queryset}

    return render(request,'menu.html', context= context)

@login_required(login_url='/login/')
def delete_receipe(request, id):
    queryset = receipe.objects.get(id = id)
    queryset.delete()
    return redirect('menu')

@login_required(login_url='/login/')
def update_receipe(request, id):
    queryset = receipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect('menu')
    context = {'receipe' : queryset}
    return render(request, 'update_receipe.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Invalid username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            print('hi')
            return redirect('menu')
    return render(request, 'login.html')

def signup_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/signup/')
        
        user = User.objects.create(
            username = username
            # password = password
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account created Successfully')

        return redirect('/signup/')
    return render(request, 'signup.html')
