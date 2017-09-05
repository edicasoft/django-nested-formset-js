from django.db import models


# parent/root model
class Parent(models.Model):
    name = models.CharField(max_length=50)


# nested set level 1
class Tab(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


# nested set level 2
class SubList(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
