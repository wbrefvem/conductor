from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotAllowed
from integrations.tasks import notify_at_task
import json
import pprint
import requests

pp = pprint.PrettyPrinter(indent=4)


class AtTaskNotificationView(View):
    template_name = 'template.html'

    def login(username='', password=''):
        resp = requests.get('https://raleighnc-it.attask-ondemand.com/attask/api/login?username=%s&password=%s' % (username, password))
        data = resp.json()['data']
        return data['sessionID']

    def logout(session_id=''):
        resp = requests.get('https://raleighnc-it.attask-ondemand.com/attask/api/logout?sessionID=%s' % session_id)
        success = resp.json()['data']['success']

        if not success:
            raise NetworkError('Logout failed!')

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        # note_string = '[GitHub] %s' % data['comment']['body']

        # session_id = self.login('will.refvem@raleighnc.gov', 'Welcome2')

        # resp = requests.post('https://raleighnc-it.attask-ondemand.com/attask/api/')

        pp.pprint(data)

        return HttpResponse('AtTask notification initiated...')

    def get(self, request, *args, **kwargs):

        notify_at_task.delay()
        return HttpResponseNotAllowed(['POST'], "405. There's nothing to GET here. Too bad!")
