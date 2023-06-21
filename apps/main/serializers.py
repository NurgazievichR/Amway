from rest_framework import serializers

from apps.products.models import Product
from apps.main.models import Main, Consultation, OrderItem
from apps.main.tasks import send_message


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']






class MainSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Main
        fields = ['name', 'gmail', 'phone_number', 'address', 'comment', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        main = Main.objects.create(**validated_data)

        for order_item_data in order_items_data:
            product_id = order_item_data['product']
            quantity = order_item_data['quantity']
            # Извлекаем продукт по его идентификатору
            product = Product.objects.get(pk=product_id.id)
            # Создаем объект OrderItem с ссылкой на продукт и связью с Main
            OrderItem.objects.create(order=main, product=product, quantity=quantity)
        
        products = main.order_items.all()
        send_message(main, products)

        return main





    

















