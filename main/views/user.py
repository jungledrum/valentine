from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.contrib.auth import (authenticate, 
                                 login as user_login,
                                 logout as user_logout)
from mongoengine.django.auth import User


def index(req):
    return HttpResponse('hah')


def show(req):
    pass


def new(req):
    pass


def create(req):
    pass


def edit(req):
    pass


def update(req):
    pass


def destroy(req):
    pass


def login(req):
    if req.method == 'GET':
        return render(req, 'user/login.html')
    elif req.method == 'POST':
        username = req.POST.get('username', '')
        password = req.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            user_login(req, user)
        else:
            return redirect(reverse('login'))
        return redirect('index')


def register(req):
    if req.method == 'GET':
        return render(req, 'user/register.html')
    elif req.method == 'POST':
        form = req.POST
        User.create_user(username=form['username'], password=form['password'])
        return redirect('index')


def logout(req):
    user_logout(req)
    return redirect('index')