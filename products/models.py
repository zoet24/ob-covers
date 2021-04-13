from django.db import models
from colorful.fields import RGBColorField


# Create your models here.
class Range(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Style(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Colour(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    rgb_colour = RGBColorField(default='0,0,0')
    rgb_background = RGBColorField(default='0,0,0')
    rgb_border = RGBColorField(default='0,0,0')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    range = models.ForeignKey('Range', null=True, blank=True, on_delete=models.SET_NULL)
    style = models.ForeignKey('Style', null=True, blank=True, on_delete=models.SET_NULL)
    colour = models.ForeignKey('Colour', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
