from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    description = models.CharField(max_length=100, blank=False, null=False)
    price = models.FloatField(default=0.99, blank=False, null=False)
    img = models.CharField(max_length=50, default="/static/img/sample.jpg")
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    on_sell = models.BooleanField(default=True)

    def __str__(self):
        return self.description


class Order(models.Model):
    # user info
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    item_cnt = models.IntegerField(default=1)

    # return the total price for current order
    def total(self):
        return self.item_cnt * self.item.price

    def __str__(self):
        return "<" + str(self.item_id) + ', ' + str(self.item_cnt) + ">"
