from django.db import models

# class PaymentMethod(models.Model):
#     name = models.CharField(max_length=200, unique=True, verbose_name='Спосіб оплати')
    
#     class Meta:
#         db_table = 'payment_method'
#         verbose_name = 'Спосіб оплати'
#         verbose_name_plural = 'Способи оплати'

#     def __str__(self):
#         return self.name

class PaymentMethod(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Спосіб оплати')
    link = models.URLField(verbose_name='Посилання на оплату', max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='payment', verbose_name='Зображення методу оплати', null=True, blank=True)
    
    class Meta:
        db_table = 'payment_method'
        verbose_name = 'Спосіб оплати'
        verbose_name_plural = 'Способи оплати'

    def __str__(self):
        return self.name
    

class Hint(models.Model):
    list = models.TextField(verbose_name='Список підказок')
    payment_method = models.ForeignKey(to=PaymentMethod, on_delete=models.CASCADE, verbose_name='Спосіб оплати')
    
    class Meta:
        db_table = 'hint'
        verbose_name = 'Підказки'
        verbose_name_plural = 'Підказки'

    def get_list(self):
        return self.list.split(';')

    def __str__(self):
        return self.payment_method.name
