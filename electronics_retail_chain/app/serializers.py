from rest_framework import serializers
from .models import Link, Contacts, Product, Network


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ('type',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = (
            "email",
            "country",
            "town",
            "street",
            "house"
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer()
    products = ProductSerializer(many=True)
    network = NetworkSerializer()

    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ('debt',)

