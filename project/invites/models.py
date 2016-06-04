from __future__ import unicode_literals

from django.db import models


class Invites(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.id)


class User(models.Model):
    invite = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(unique=True)
    login = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)

    class Meta:
        ordering = ['login']

    def __str__(self):
        return "{}:{}".format(self.email, self.login)
