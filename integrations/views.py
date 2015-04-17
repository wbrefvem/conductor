from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotAllowed


class AtTaskNotificationView(View):
    template_name = 'template.html'

    def post(self, request, *args, **kwargs):

        return HttpResponse('AtTask notification initiated...')

    def get(self, request, *args, **kwargs):

        return HttpResponseNotAllowed(['POST'], "This url is an event handler and doesn't accept GET requests.")
