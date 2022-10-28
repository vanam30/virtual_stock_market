from django.db import models

# Create your models here.
class Pending_Buy_Order(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()
    user = models.OneToOneField()
