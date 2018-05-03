from django.db import models

# Create your models here.


class Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=10)


class Item(models.Model):
    ITEM_TYPE = (
        ('V','Villa'),
        ('P','Plot'),
        ('F','Flat'),
    )
    CITY = (
        ('KOCHI','kochi'),
        ('TRIVANDRUM','trivandrum'),
        ('KOTTAYAM','kottayam'),
        ('THRISSUR','thrissur'),
        ('KOZHIKODE','kozhikode'),

    )
    item_title = models.CharField(max_length=50)
    item_description = models.CharField(max_length=90)
    item_type = models.CharField(max_length=1, choices=ITEM_TYPE)
    item_images = models.ImageField(upload_to='realapp/images')
    name = models.CharField(max_length=15)
    contact_phone_no = models.IntegerField()
    city = models.CharField(max_length=20, choices=CITY)






