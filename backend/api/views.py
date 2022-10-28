from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint' : '/api/users/',
            'method' : 'GET/POST'
        },
        {
            'Endpoint' : '/api/codes/',
            'method' : 'GET/POST'
        },
    ]
    return Response(routes) #shows what queries can be made
