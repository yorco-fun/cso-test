from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=250, verbose_name='Район')

    class Meta:
        db_table = 'region'
        verbose_name = 'Район'
        verbose_name_plural = 'Райони'

    def __str__(self):
        return self.name
    
class TariffCategory(models.Model):
    name = models.CharField(max_length=250, verbose_name='Категорія тарифів')

    class Meta:
        db_table = 'tariff_category'
        verbose_name = 'Категорію тарифів'
        verbose_name_plural = 'Категорії тарифів'

    def __str__(self):
        return self.name
    
class BuildingType(models.Model):
    name = models.CharField(max_length=250, verbose_name='Тип нерухомості')

    class Meta:
        db_table = 'building_type'
        verbose_name = 'Тип нерухомості'
        verbose_name_plural = 'Тип нерухомості'

    def __str__(self):
        return self.name

class Tariffs(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Назва')
    price = models.IntegerField(null=True, verbose_name="Ціна")
    speed = models.CharField(max_length=100, null=True, verbose_name="Швидкість")
    text = models.TextField(null=True, verbose_name='Опис')
    building_type = models.ForeignKey(to=BuildingType, null=True, on_delete=models.CASCADE, verbose_name='Тип нерухомості')
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE, verbose_name='Район')
    type = models.ForeignKey(to=TariffCategory, on_delete=models.CASCADE, verbose_name='Категорія тарифів')
    
    class Meta:
        db_table = 'tariff'
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифи'

    def __str__(self):
        return self.title
    
class Business(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Назва')
    price = models.IntegerField(null=True, verbose_name="Ціна")
    speed = models.CharField(max_length=100, null=True, verbose_name="Швидкість")
    text = models.TextField(null=True, verbose_name='Опис')
    
    class Meta:
        db_table = 'business'
        verbose_name = 'Бізнес тариф'
        verbose_name_plural = 'Бізнес тарифи'

    def __str__(self):
        return self.title