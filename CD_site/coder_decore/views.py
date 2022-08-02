from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница CODER DECORE")

def categories(request):
    return HttpResponse("<h1>Статья по категориям </h1>")