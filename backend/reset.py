from myUser.models import Person,Pending_Sell_Order,Pending_Buy_Order,Transaction,MarketPrice

if __name__ == '__main__':
    Person.objects.filter(name='A').update(stocks=10,fiat=5000)
    Person.objects.filter(name='B').update(stocks=20,fiat=3000)
    Person.objects.filter(name='C').update(stocks=30,fiat=6000)
    Person.objects.filter(name='D').update(stocks=15,fiat=2500)
    Person.objects.filter(name='E').update(stocks=40,fiat=2000)
    Pending_Buy_Order.objects.all().delete()
    Pending_Sell_Order.objects.all().delete()
    Transaction.objects.all().delete()
    MarketPrice.objects.all().delete()
