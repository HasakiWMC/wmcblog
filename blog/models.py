from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)


class Article(models.Model):
    pid = models.IntegerField(default=0)
    title = models.CharField(default="aaa", max_length=200)
    content = models.TextField(default="aaa", max_length=200)
    author = models.ForeignKey(Author)
