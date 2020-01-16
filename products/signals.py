from django.db.models import signals
from django.dispatch import receiver
from django.utils.text import slugify

from core import utils
from products import models as pm

@receiver(signals.pre_save, sender=pm.Product)
def add_slug_to_product(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = utils.generate_random_string()
        instance.slug = f"{slug}-{random_string}"