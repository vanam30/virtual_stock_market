from rest_framework.response import Response
from myUser.models import Person
from .serializers import PersonSerializers
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_user_portfolio(request):
    person = PersonSerializers(Person.objects.all(),many=True)
    return Response(person.data) #shows what queries can be made
