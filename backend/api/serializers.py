from rest_framework.serializers import ModelSerializer
from myUser.models import Person

class PersonSerializers(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
