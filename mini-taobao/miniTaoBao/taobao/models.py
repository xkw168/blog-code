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
