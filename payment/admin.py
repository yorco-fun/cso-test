from django.contrib import admin

from payment.models import Hint, PaymentMethod

admin.site.register(PaymentMethod)
admin.site.register(Hint)