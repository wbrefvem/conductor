from django.db import models
from django.contrib.auth.models import User


class GitHubAccount(models.Model):
    user = models.ForeignKey(User)
    github_id = models.IntegerField()


class AtTaskAccount(models.Model):
    user = models.ForeignKey(User)
    attask_id = models.IntegerField()


class Worker(models.Model):
    github_account = models.ForeignKey(GitHubAccount)
    attask_account = models.ForeignKey(AtTaskAccount)
