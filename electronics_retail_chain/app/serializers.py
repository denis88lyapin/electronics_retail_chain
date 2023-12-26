from rest_framework import serializers
from .models import Link, Contacts, Product, Network
from .validators import SupplierValidator


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ('type',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    level = serializers.IntegerField(read_only=True, source='suppliers.count')

    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ('debt',)
        validators = [SupplierValidator(supplier_field='supplier', network_field='network')]
