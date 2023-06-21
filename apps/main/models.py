from django.db import models
from django.core.validators import validate_email

from apps.products.models import Product
from utils.NumberValidator import kg_phone_validator


class Main(models.Model):
    """
    Model for sending message to gmail
    """
    name = models.CharField(
        max_length=256,
        verbose_name='name'
    )
    gmail = models.EmailField(
        validators=[validate_email]
    )
    phone_number = models.CharField(
        max_length=256,
        verbose_name='phone_number',
        validators=[kg_phone_validator]
    )
    address = models. CharField(
        max_length=256,
        verbose_name='address'
    )
    comment = models.TextField(
        verbose_name='comment'
    )
    with_delivery = models.BooleanField(verbose_name='Доставка', default=False)


    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        verbose_name = 'main'
        verbose_name_plural = 'Mains'



class OrderItem(models.Model):
    order = models.ForeignKey(Main, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField(default=1)


class Consultation(models.Model):
    """
    Model for sending message to gmail about consultations
    """
    name = models.CharField(
        max_length=256,
        verbose_name='name'
    )
    phone_number = models.CharField(
        max_length=256,
        verbose_name='phone_number',
        validators=[kg_phone_validator]
    )
    gmail = models.EmailField(
        validators=[validate_email]
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )

    def __str__(self):
        return f'{self.id} -- {self.name}'
    
    class Meta:
        verbose_name = 'consultation'
        verbose_name_plural = 'Consultations'







