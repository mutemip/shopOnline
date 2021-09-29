from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE,
                                     related_name="products")
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
