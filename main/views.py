from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from blog.models import Articles
from main.models import FAQ, Vacancy
from tariffs.models import Tariffs

@method_decorator(cache_page(60 * 30), name='dispatch')
class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
        context['latest_articles'] = Articles.objects.all().order_by('-date')[:4]
        context['slider_articles'] = Articles.objects.filter(category__name='Акція').order_by('-date')[:5]
        context['tariffs'] = Tariffs.objects.all().order_by('?')[:3]
        context['faqs'] = FAQ.objects.all()
        return context


@method_decorator(cache_page(60 * 60 * 24), name='dispatch')
class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Про нас'
        return context

@method_decorator(cache_page(60 * 60), name='dispatch')
class ContactsView(TemplateView):
    template_name = 'main/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        context['title'] = 'Контакти та вакансії'
        return context
    
class Error404(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Сторінка не знайдена'
        return context

class Error500(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Помилка сервера'
        return context