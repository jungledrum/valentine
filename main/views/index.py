from django.http import HttpResponse
from django.shortcuts import render

from main.models.user import User


def index(req):
    user = User('bo', 17, '2')
    return render(req, 'index.html', {'user': user})


def hi(req):
    return HttpResponse('hi')