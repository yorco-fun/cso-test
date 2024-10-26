from django.contrib import admin

from tariffs.models import BuildingType, Business, Tariffs, Region, TariffCategory


admin.site.register(Tariffs)
admin.site.register(Region)
admin.site.register(TariffCategory)
admin.site.register(BuildingType)
admin.site.register(Business)