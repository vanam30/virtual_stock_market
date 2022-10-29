from rest_framework.response import Response
from myUser.models import Person, Pending_Buy_Order, Pending_Sell_Order, Transaction, MarketPrice
from .serializers import PersonSerializers, BuyOrderSerializer, SellOrderSerializer, TransactionSerializer, MarketPriceSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'url': 'http://127.0.0.1:8000/order',
            'payload': 'GET : Requirements for Post method. POST : Add new order in market',
            'method': '{GET,POST}'
        },
        {
            'url': 'http://127.0.0.1:8000/user',
            'payload': 'User Portfolio',
            'method': 'GET'
        },
        {
            'url': 'http://127.0.0.1:8000/price',
            'payload': 'Sends Current Market Price as JSON file',
            'method': 'GET'
        },
        {
            'url': 'http://127.0.0.1:8000/sell',
            'payload': 'Sends Pending sells',
            'method': 'GET'
        },
        {
            'url': 'http://127.0.0.1:8000/buy',
            'payload': 'Sends Pending buys',
            'method': 'GET'
        },
        {
            'url': 'http://127.0.0.1:8000/transaction',
            'payload': 'Sends Transaction History',
            'method': 'GET'
        },
        {
            'url': 'http://127.0.0.1:8000/graph',
            'payload': 'Sends Y-Coordinates of Graph',
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
            return Response({'error': 'buy_sell info not found', 'error_code': 1})
        if buy_or_sell != 'buy' and buy_or_sell != 'sell':
            return Response({'error': 'wrong choice in buy_or_sell', 'error_code': 2})

        if user == None:
            return Response({'error': 'user info not found', 'error_code': 3})
        if len(Person.objects.filter(name=user)) == 0:
            return Response({"error": "user not found in database", 'error_code': 4})
        user = Person.objects.filter(name=user).first()

        if order_type == None:
            return Response({"error": "order_type not found", 'error_code': 5})
        if order_type != "limit" and order_type != "market":
            return Response({"error": "Wrong Choice for order_type", 'error_code': 6})

        if stock_amount == None:
            return Response({"error": "stock_amount not found", 'error_code': 7})

        try:
            stock_amount = int(stock_amount)
        except:
            return Response({"error": "Wrong type of stock amount", 'error_code': 8})

        if order_type == 'limit':
            if price == None:
                return Response({"error": "price not found", 'error_code': 9})
            try:
                price = float(price)
            except:
                return Response({"error": "Wrong type of price", 'error_code': 10})

            # TODO : Apply limit rules
            content = []
            if buy_or_sell == 'buy':
                # TODO: Search for match in Pending Sells
                to_save = []
                to_delete = []
                user_selled = {}
                sellers = Pending_Sell_Order.objects.filter(price=price)
                for seller in sellers:
                    if stock_amount <= 0:
                        break
                    if seller.quantity == stock_amount:
                        current_quantity = user_selled.get(seller.owner, 0)
                        if current_quantity == 0:
                            user_selled[seller.owner] = 0
                        user_selled[seller.owner] += stock_amount
                        content.append({
                            "action": "remove_pending_sell",
                            "payload": {
                                "id": seller.id,
                            }
                        })
                        to_delete.append(seller.id)
                        stock_amount = 0

                    elif seller.quantity > stock_amount:
                        current_quantity = user_selled.get(seller.owner, 0)
                        if current_quantity == 0:
                            user_selled[seller.owner] = 0
                        user_selled[seller.owner] += stock_amount
                        content.append({
                            "action": "update_pending_sell",
                            "payload": {
                                "id": seller.id,
                                "quantity": seller.quantity - stock_amount
                            }
                        })
                        to_save.append(
                            {"id": seller.id, "quantity": seller.quantity - stock_amount})
                        stock_amount = 0
                    else:
                        current_quantity = user_selled.get(seller.owner, 0)
                        if current_quantity == 0:
                            user_selled[seller.owner] = 0
                        user_selled[seller.owner] += seller.quantity
                        content.append({
                            "action": "remove_pending_sell",
                            "payload": {
                                "id": seller.id,
                            }
                        })
                        to_delete.append(seller.id)
                        stock_amount -= seller.quantity
                buyer_quantity = 0
                buyer_price = 0
                once = 1
                for key in user_selled:
                    trans = Transaction(seller=key, buyer=str(
                        user), quantity=user_selled[key], price=price)
                    trans.save()
                    content.append({
                        "action": "add_transaction",
                        "payload": {
                            "id": trans.id,
                            "seller": trans.seller,
                            "buyer": trans.buyer,
                            "quantity": trans.quantity,
                            "price": trans.price,
                            "date": trans.date
                        }
                    })
                    if once == 1:
                        MarketPrice(price=trans.price).save()
                        content.append({
                            "action": "change_market_price",
                            "payload": {
                                "market_price" : trans.price
                            }
                        })
                        once = 0
                    buyer_quantity += trans.quantity
                    buyer_price += (trans.quantity * trans.price)
                    person = Person.objects.filter(name=trans.seller).first()
                    new_stocks = person.stocks - trans.quantity
                    new_fiat = person.fiat + (trans.quantity * trans.price)
                    Person.objects.filter(name=trans.seller).update(
                        stocks=new_stocks, fiat=new_fiat)
                    content.append({
                        "action": "update_user",
                        "payload": {
                            "name": trans.seller,
                            "stocks": new_stocks,
                            "fiat": new_fiat
                        }
                    })

                if buyer_quantity != 0:
                    person = Person.objects.filter(name=str(user)).first()
                    new_stocks = person.stocks + buyer_quantity
                    new_fiat = person.fiat - buyer_price

                    Person.objects.filter(name=str(user)).update(
                        stocks=new_stocks, fiat=new_fiat)
                    content.append({
                        "action": "update_user",
                        "payload": {
                            "name": person.name,
                            "stocks": new_stocks,
                            "fiat": new_fiat
                        }
                    })

                for key in to_delete:
                    Pending_Sell_Order.objects.filter(id=key).delete()

                for key in to_save:
                    Pending_Sell_Order.objects.filter(
                        id=key['id']).update(quantity=key['quantity'])

                if stock_amount > 0:
                    pending_buy = Pending_Buy_Order(quantity=stock_amount,
                                                    price=price, owner=str(user))
                    pending_buy.save()
                    content.append({
                        "action": "add_pending_buy",
                        "payload": {
                            "id": pending_buy.id,
                            "user": pending_buy.owner,
                            "quantity": pending_buy.quantity,
                            "price": pending_buy.price
                        }
                    })
            else:
                
                

                if stock_amount > 0:
                    pending_sell = Pending_Sell_Order(quantity=stock_amount,
                                                    price=price, owner=str(user))
                    pending_sell.save()

                    content.append({
                        "action": "add_pending_sell",
                        "payload": {
                            "id": pending_sell.id,
                            "user": pending_sell.owner,
                            "quantity": pending_sell.quantity,
                            "price": pending_sell.price
                        }
                    })

            return Response(content)
        else:
            # TODO : Apply market rules

            if buy_or_sell == 'buy':
                pass
            else:
                pass
            return Response({"success": "market order"})


@api_view(['GET'])
def get_market_price(request):
    if len(MarketPrice.objects.all()) == 0:
        MarketPrice(price=0).save()
    market_price = MarketPrice.objects.all().last()
    serializer = MarketPriceSerializer(market_price, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_graph(request):
    if len(MarketPrice.objects.all()) == 0:
        MarketPrice(price=0).save()
    serializer = MarketPriceSerializer(MarketPrice.objects.all(), many=True)
    return Response(serializer.data)
