from django.contrib import admin
from django.utils.html import format_html
from rest_framework.reverse import reverse

from .models import Network, Contacts, Product, Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'supplier', 'products_list', 'debt', 'created_at', 'network', 'supplier_url')
    list_filter = ('contacts__town', 'network__type')
    search_fields = ('name', 'contacts__town')
    list_select_related = ('contacts', 'supplier', 'network')
    actions = ['clear_debt']

    def supplier_url(self, obj):
        if obj.supplier:
            url = reverse('admin:app_link_change', args=[obj.supplier.id])
            return format_html("<a href='{}'>{}</a>", url, obj.supplier)

    def products_list(self, obj):
        return ",\n ".join([product.name for product in obj.products.all()])

    @admin.action(description='Clear debt')
    def clear_debt(self, request, queryset):
        queryset.update(debt=None)


admin.site.register(Network)
admin.site.register(Contacts)
admin.site.register(Product)
admin.site.register(Link, LinkAdmin)
