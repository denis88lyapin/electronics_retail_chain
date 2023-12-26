from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import LinkFilter
from .models import Link, Contacts, Product
from .serializers import LinkSerializer, ContactSerializer, ProductSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    filterset_class = LinkFilter


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
