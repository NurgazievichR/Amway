from django.db import models


class Category(models.Model):
    """
    Model for categories
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    image = models.ImageField(
        upload_to='category_images/',
        verbose_name='image'
    )

    def __str__(self):
        return f'{self.id} -- {self.title}'
    
    class Meta:
        verbose_name = 'category' 
        verbose_name_plural = 'Categories'
