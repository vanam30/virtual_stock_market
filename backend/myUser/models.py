from email.policy import default
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
    added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.added)


class Pending_Sell_Order(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()
    added = models.DateField(auto_now_add=True)
    owner = models.OneToOneField(
        Person, related_name='pending_sell_order', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.added)


class Transaction(models.Model):
    seller = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='trans_seller')
    buyer = models.ForeignKey(Person, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.date) + " (" + str(self.seller)+" -> "+str(self.buyer)+")"
