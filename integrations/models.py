from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=256)


class Integration(models.Model):
    services = models.ManyToManyField(Service)


class Worker(models.Model):
    user = models.ForeignKey(User)


class Account(models.Model):
    service = models.ForeignKey(Service)
    worker = models.OneToOneField(Worker)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=128)
