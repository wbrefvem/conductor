from rest_framework import viewsets
from status import models
from api import serializers, renderers, parsers


class BaseViewSet(viewsets.ModelViewSet):
    renderer_classes = (renderers.JSONRenderer,)
    parser_classes = (parsers.JSONParser,)


class StatusViewSet(BaseViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
