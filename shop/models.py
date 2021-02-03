from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return self.manufacturer

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Supply(models.Model):
    number = models.CharField(max_length=12)
    date = models.DateTimeField()

    def __str__(self):
        return self.number

    

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', null=True, on_delete= models.PROTECT)
    specifications = models.TextField(max_length=400)
    manufacturer = models.ForeignKey('Manufacturer', null=True, on_delete= models.PROTECT)
    price = models.IntegerField()
    supply = models.ForeignKey('Supply', null=True, on_delete= models.PROTECT)

    def __str__(self):
        return self.title


class Order(models.Model):
    number = models.IntegerField()
    product = models.ForeignKey('Product', on_delete= models.PROTECT)
    buyer = models.ForeignKey('Buyer', on_delete= models.PROTECT)
    date = models.DateTimeField()

    def __str__(self):
        return self.number



