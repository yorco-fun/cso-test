from django.shortcuts import render
from django.views import View
from django.http import Http404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from tariffs.models import Business, Tariffs


@method_decorator(cache_page(60 * 60), name='dispatch')
class TariffsView(View):
    def get(self, request):
        tariffs = Tariffs.objects.all().order_by('price')

        if not tariffs.exists():
            raise Http404("Немає доступних тарифів")

        context = {
            'title': 'Тарифи',
            'tariffs': tariffs
        }
        return render(request, 'tariffs/tariffs.html', context)


@method_decorator(cache_page(60 * 60), name='dispatch')
class BusinessView(View):
    def get(self, request):
        business = Business.objects.all().order_by('price')

        if not business.exists():
            raise Http404("Немає доступних тарифів для бізнесу")

        context = {
            'title': 'Для бізнесу',
            'business': business
        }
        return render(request, 'tariffs/business.html', context)
