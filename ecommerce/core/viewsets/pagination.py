from collections import OrderedDict

from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class CustomPagination(CursorPagination):
    cursor_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_size = 5

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', 1),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'number'
                },
                'next': {
                    'type': 'string',
                    'nullable': True,
                },
                'previous': {
                    'type': 'string',
                    'nullable': True,
                },
                'results': schema,
            },
        }
