from rest_framework import serializers

from apps.categories.models import Category
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    product_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
            'product_data'
        )

    def get_product_data(self, instance):
        products = Product.objects.filter(category__id=instance.id)
        serializer = ProductSerializer(products, many=True)
        return serializer.data
