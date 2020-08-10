from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    img_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.TextField()
    description = models.TextField()
    discount = models.FloatField()
