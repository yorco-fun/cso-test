from django.urls import path
from tariffs.views import TariffsView, BusinessView

app_name = 'tariffs'

urlpatterns = [
    path('', TariffsView.as_view(), name='index'),
    path('business/', BusinessView.as_view(), name='business'),
]
