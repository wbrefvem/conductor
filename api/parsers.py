from rest_framework.parsers import BaseParser
import json


class JSONParser(BaseParser):
    media_type = 'application/json'

    def parse(self, stream, media_type, parser_context):

        model = parser_context['view'].get_queryset().first().__class__.__name__
        data = json.loads(stream.read())

        return data[model.lower()]
