from django.db import models
from colorfield.fields import ColorField


# Create your models here.
class Range(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
                                     blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Style(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
                                     blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Colour(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
                                     blank=True)
    hex_colour = ColorField(default='#FFFFFF')
    hex_background = ColorField(default='#FFFFFF')
    hex_border = ColorField(default='#FFFFFF')

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254,
                           blank=True)
    name = models.CharField(max_length=254)
    range = models.ForeignKey('Range', null=True,
                              blank=True, on_delete=models.SET_NULL)
    style = models.ForeignKey('Style', null=True,
                              blank=True, on_delete=models.SET_NULL)
    colour = models.ForeignKey('Colour', null=True,
                               blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)
    image_url = models.URLField(max_length=1024, blank=True)
    unavailable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
