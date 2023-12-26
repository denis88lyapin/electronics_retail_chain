from rest_framework.serializers import ValidationError
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

from .models import Network


class SupplierValidator:
    def __init__(self, supplier_field, network_field):
        self.supplier_field = supplier_field
        self.network_field = network_field

    def __call__(self, values):
        supplier = values.get(self.supplier_field)
        network = values.get(self.network_field)
        if str(supplier.network) == Network.TYPE_FACTORY and str(network) == Network.TYPE_FACTORY:
            raise ValidationError({
                self.supplier_field: 'Завод должен быть 0-м уровнем сети!',
            })
