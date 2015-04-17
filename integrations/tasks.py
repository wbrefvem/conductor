import requests

from celery import shared_task


@shared_task
def notify_at_task(data=None):

    resp = requests.get('https://raleighnc-it.attask-ondemand.com/attask/api/login?username=will.refvem@raleighnc.gov&password=Welcome2')

    print resp.status_code
    print resp.json()
