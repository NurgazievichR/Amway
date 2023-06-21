from django.db import models


class Review(models.Model):
    """
    Model for reviews
    """
    name = models.CharField(
        max_length=256,
        verbose_name='name'
    )
    comment = models.TextField(
        verbose_name='comment'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'Reviews'
