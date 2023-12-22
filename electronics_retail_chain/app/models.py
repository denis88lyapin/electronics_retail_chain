from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class Network(models.Model):
    TYPE_FACTORY = 'factory'
    TYPE_RETAIL = 'retail'
    TYPE_ENTREPRENEUR = 'entrepreneur'
    TYPES = (
        (TYPE_FACTORY, 'Завод'),
        (TYPE_RETAIL, 'Розничная сеть'),
        (TYPE_ENTREPRENEUR, 'Предприниматель'),
    )
    type = models.CharField(max_length=15, verbose_name='сеть', choices=TYPES)


class Contacts(models.Model):
    email = models.EmailField(max_length=70, unique=True, verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='страна')
    town = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house = models.CharField(max_length=30, verbose_name='номер дома')

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    date = models.DateField(verbose_name='дата выхода на рынок')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Link(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='контакты')
    products = models.ManyToManyField(Product, verbose_name='продукт')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='задолженность перед поставщиком', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    network = models.ForeignKey(Network, on_delete=models.CASCADE, verbose_name='сеть')

    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"
