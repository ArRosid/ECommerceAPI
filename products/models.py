from django.db import models
from core import utils

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to=utils.upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title