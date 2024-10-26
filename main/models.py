from django.db import models

class Main(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True, verbose_name='Заголовок')
    sub_title = models.CharField(max_length=200, unique=True, null=True, verbose_name='Підзаголовок')
    text = models.TextField( null=True, verbose_name='Текст')


    class Meta:
        db_table = 'main'
        verbose_name = 'Головні статті'
        verbose_name_plural = 'Головні статті'

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True, verbose_name='Заголовок')
    text = models.TextField(unique=True, null=True, verbose_name='Текст')


    class Meta:
        db_table = 'faq'
        verbose_name = 'Часті питання'
        verbose_name_plural = 'Часті питання'

    def __str__(self):
        return self.title
    
class Vacancy(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name="Посада")
    responsibilities = models.TextField(null=True, verbose_name="Обов'язки")
    requirements = models.TextField(null=True, verbose_name="Вимоги")
    conditions = models.TextField(null=True, verbose_name="Умови роботи")
  
    class Meta:
        db_table = 'vacancy'
        verbose_name = 'Вакансію'
        verbose_name_plural = 'Вакансії'

    def get_responsibilities_list(self):
        return self.responsibilities.split(';')

    def get_requirements_list(self):
        return self.requirements.split(';')

    def get_conditions_list(self):
        return self.conditions.split(';')


    def __str__(self):
        return self.title
    