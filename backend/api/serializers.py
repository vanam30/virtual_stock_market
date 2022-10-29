from rest_framework.serializers import ModelSerializer, DateTimeField,Serializer,FloatField
from myUser.models import MarketPrice, Person, Pending_Sell_Order, Pending_Buy_Order, Transaction


class PersonSerializers(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class BuyOrderSerializer(ModelSerializer):
    class Meta:
        model = Pending_Buy_Order
        fields = '__all__'


class SellOrderSerializer(ModelSerializer):
    class Meta:
        model = Pending_Sell_Order
        fields = '__all__'


class TransactionSerializer(ModelSerializer):
    date = DateTimeField()
    class Meta:
        model = Transaction
        fields = '__all__'


class MarketPriceSerializer(Serializer):
    date = DateTimeField()
    price = FloatField()