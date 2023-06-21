from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response


from apps.main.models import Main, Consultation, OrderItem
from apps.main.serializers import MainSerializer, ConsultationSerializer, OrderItemSerializer


class MainApiViewSet(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer



class ConsultationApiViewSet(ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer



