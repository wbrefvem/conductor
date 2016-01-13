import requests

from celery import shared_task
from integrations.models import Worker
from github3 import GitHub


@shared_task
def update_attask(data=None):

    for worker in Worker.objects.all():

        gh_user = worker.github_account.user.username
        gh_pass = worker.github_account.user.password
        at_user = worker.attask_account.user.username
        at_pass = worker.attask_account.user.password

        gh = GitHub(gh_user, gh_pass)

        session = requests.Session()
        resp = session.get('https://raleighnc-it.attask-ondemand.com/attask/api/login?username=%s&password=%s', (at_user, at_pass))

        print resp.status_code
        print resp.json()
