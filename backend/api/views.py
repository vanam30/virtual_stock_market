from rest_framework.response import Response
from myUser.models import Person, Pending_Buy_Order, Pending_Sell_Order, Transaction
from .serializers import PersonSerializers, BuyOrderSerializer, SellOrderSerializer, TransactionSerializer
from rest_framework.decorators import api_view

MARKET_PRICE = 100
PREVIOUS_PRICE = [MARKET_PRICE]


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'url': 'http://127.0.0.1:8000/order',
            'desc': 'GET : Requirements for Post method. POST : Add new order in market',
            'method': '{GET,POST}'
        },
        {
            'url': 'http://127.0.0.1:8000/user',
            'desc': 'User Portfolio',
            'method': 'GET'
        },
        {
            'url': 'http://127.0.0.1:8000/price',
            'desc': 'Sends Current Market Price as JSON file',
            'method': 'GET'
        },
        {
            'url': 'http://127.0.0.1:8000/sell',
            'desc': 'Sends Pending sells',
            'method': 'GET'
        },
        {
            'url': 'http://127.0.0.1:8000/buy',
            'desc': 'Sends Pending buys',
            'method': 'GET'
        },
        {
            'url': 'http://127.0.0.1:8000/transaction',
            'desc': 'Sends Transaction History',
            'method': 'GET'
        },
        {
            'url': 'http://127.0.0.1:8000/graph',
            'desc': 'Sends Y-Coordinates of Graph',
            'method': 'GET'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def get_user_portfolio(request):
    person = PersonSerializers(Person.objects.all(), many=True)
    return Response(person.data)


@api_view(['GET'])
def get_pending_buy(request):
    pending_buys = BuyOrderSerializer(
        Pending_Buy_Order.objects.all(), many=True)
    return Response(pending_buys.data)


@api_view(['GET'])
def get_pending_sell(request):
    pendind_sells = SellOrderSerializer(
        Pending_Sell_Order.objects.all(), many=True)
    return Response(pendind_sells.data)


@api_view(['GET'])
def get_transactions(request):
    transactions = TransactionSerializer(
        Transaction.objects.all(), many=True)
    return Response(transactions.data)


@api_view(['GET', 'POST'])
def add_new_order(request):
    if request.method == 'GET':
        requirements = {
            'buy_or_sell': 'buy/sell',
            'user': 'A/B/C/...',
            'order_type': 'limit/market',
            'stock_amount': 'interger value',
            'price': 'float value (not required for order_type = market)'
        }
        return Response(requirements)
    elif request.method == 'POST':
        buy_or_sell = request.data.get('buy_or_sell', None)
        user = request.data.get('user', None)
        order_type = request.data.get('order_type', None)
        stock_amount = request.data.get('stock_amount', None)
        price = request.data.get('price', None)

        if buy_or_sell == None:
            return Response({'error': 'buy_sell info not found'})
        if buy_or_sell != 'buy' and buy_or_sell != 'sell':
            return Response({'error': 'wrong choice in buy_or_sell'})

        if user == None:
            return Response({'error': 'user info not found'})
        if len(Person.objects.filter(name=user)) == 0:
            return Response({"error": "user not found in database"})
        user = Person.objects.filter(name=user).first()

        if order_type == None:
            return Response({"error": "order_type not found"})
        if order_type != "limit" and order_type != "market":
            return Response({"error": "Wrong Choice for order_type"})

        if stock_amount == None:
            return Response({"error": "stock_amount not found"})

        try:
            stock_amount = int(stock_amount)
        except:
            return Response({"error": "Wrong type of stock amount"})

        if order_type == 'limit':
            if price == None:
                return Response({"error": "price not found"})
            try:
                price = float(price)
            except:
                return Response({"error": "Wrong type of price"})

            # TODO : Apply limit rules

            if buy_or_sell == 'buy':
                Pending_Buy_Order(quantity=stock_amount,
                                  price=price, owner=user).save()
            else:
                Pending_Sell_Order(quantity=stock_amount,
                                   price=price, owner=user).save()

            return Response({"success": "ok"})
        else:
            # TODO : Apply market rules

            if buy_or_sell == 'buy':
                pass
            else:
                pass
            return Response({"success": "market order"})


@api_view(['GET'])
def get_market_price(request):
    global MARKET_PRICE
    global PREVIOUS_PRICE

    ################################# -> TESTING PURPOSE
    MARKET_PRICE += 1
    PREVIOUS_PRICE.append(MARKET_PRICE)
    #################################

    return Response({'market_price': MARKET_PRICE})


@api_view(['GET'])
def get_graph(request):
    return Response(PREVIOUS_PRICE)
