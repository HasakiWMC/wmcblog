from datetime import date
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from blog.models import *


def hello(request, offset):
    # return HttpResponse('<h1>Hello wmc911: %s</h1>' % offset)
    name = 'sundy'
    age = 18
    return render(request, 'hello.html', locals())


def index(request):
    d = date.today()
    articles = Article.objects.all()
    return render(request, 'index.html', locals())


def article(request, pid):
    article = Article.objects.get(pid=pid)
    return render(request, 'article.html', locals())


def index2(request):
    d = date.today()
    articles = Article.objects.all()
    return render(request, 'index2.html', locals())


def article2(request, pid):
    article = Article.objects.get(pid=pid)
    return render(request, 'article2.html', locals())
