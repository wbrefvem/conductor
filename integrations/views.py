from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotAllowed
from integrations.tasks import notify_at_task
import json


class AtTaskNotificationView(View):
    template_name = 'template.html'

    def post(self, request, *args, **kwargs):
        print dir(request)

        return HttpResponse('AtTask notification initiated...')

    def get(self, request, *args, **kwargs):

        notify_at_task.delay()
        return HttpResponseNotAllowed(['POST'], "405. There's nothing to GET here. Too bad!")
