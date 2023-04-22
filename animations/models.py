from django.db import models


class Animation(models.Model):
    name=models.CharField(max_length=300)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)


class Offer(models.Model):
    code=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()

class Contacts(models.Model):
    email=models.EmailField(max_length=299)
    number=models.BigIntegerField()
    message=models.TextField()
    address=models.TextField()
    name=models.CharField(max_length=300)

class Register(models.Model):
    email=models.EmailField(max_length=299)
    number=models.BigIntegerField()
    password=models.TextField()
    name=models.CharField(max_length=300)


class News(models.Model):
    email=models.EmailField(max_length=299)





