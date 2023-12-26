import django_filters
from .models import Link


class LinkFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(field_name="contacts__country", lookup_expr="icontains",)

    class Meta:
        model = Link
        fields = ("contacts__country",)
