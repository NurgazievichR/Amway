from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models import Product
from apps.main.models import Main, Consultation, OrderItem
from apps.main.tasks import send_message, send_message_about_consultation





@receiver(post_save, sender=Consultation)
def handle_signal_consultation_created(instance, created, **kwargs):
    if created:
        information = Consultation.objects.get(id = instance.id)
        send_message_about_consultation(information)
