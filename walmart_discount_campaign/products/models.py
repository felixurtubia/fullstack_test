# from django.db import models
from djongo import models


class Product(models.Model):
    _id = models.ObjectIdField()
    id = models.IntegerField()
    brand = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.IntegerField()

    def get_half_price(self):
        p = round(self.price / 2)
        return '${:,.0f}'.format(p).replace(',', '.')

    def get_price(self):
        return '${:,.0f}'.format(self.price).replace(',', '.')
