from django.db import models

# Create your models here.


class Medicine(models.Model):
    product_img = models.ImageField(upload_to="images")
    product_price = models.IntegerField()
    product_name = models.CharField(max_length=700)

    def __str__(self):
        return self.product_name


class Vitamins(models.Model):
    product_img = models.ImageField(upload_to="images")
    product_price = models.IntegerField()
    product_name = models.CharField(max_length=700)

    def __str__(self):
        return self.product_name


class Contacts(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=1000)
    t_o_m = models.CharField(max_length=200, default="none")
    message = models.TextField()

    def __str__(self):
        return self.name


class Log(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class New(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=1000)

    def __str__(self):
        return self.name
