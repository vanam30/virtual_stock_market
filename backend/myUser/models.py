from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=32)
    stocks = models.IntegerField(default=0)
    fiat = models.FloatField(default=0)

    def __str__(self):
        return str(self.name)


class Pending_Buy_Order(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=32)

    def __str__(self):
        return str(self.added)


class Pending_Sell_Order(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=32)

    def __str__(self):
        return str(self.added)


class Transaction(models.Model):
    seller = models.CharField(max_length=32)
    buyer = models.CharField(max_length=32)
    quantity = models.IntegerField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date) + " (" + str(self.seller)+" -> "+str(self.buyer)+")"


class MarketPrice(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()

    def __str__(self) -> str:
        return str(self.price) + "->" + str(self.date)