from django.shortcuts import render
from django.views import View
from payment.models import Hint
from django.http import Http404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@method_decorator(cache_page(60 * 30), name='dispatch')
class PaymentView(View):
    def get(self, request):
        hint_list = Hint.objects.all()

        if not hint_list.exists():
            raise Http404("Немає доступних підказок для оплати")

        context = {
            'title': 'Оплата послуг',
            'hint_list': hint_list
        }
        return render(request, 'payment/payment.html', context)
