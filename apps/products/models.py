from django.db import models
from django.core.validators import MinValueValidator

from apps.categories.models import Category


class Product(models.Model):
    """
    Model for products
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    image = models.ImageField(
        upload_to='product_images/',
        verbose_name='image'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='category',
        verbose_name='category',
        null=True,
        blank=True
    )
    price = models.PositiveSmallIntegerField(
        default=0, 
        validators=[MinValueValidator(0)],
        verbose_name='price'
    )
    description = models.TextField(
        verbose_name='description'
    )

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'Products'
