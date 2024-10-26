from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.http import Http404
from blog.models import Articles


@method_decorator(cache_page(60 * 30), name='dispatch')
class BlogView(View):
    def get(self, request):
        page = request.GET.get('page', 1)
        articles = Articles.objects.all()

        paginator = Paginator(articles, 4)
        try:
            current_page = paginator.page(int(page))
        except PageNotAnInteger:
            current_page = paginator.page(1)
        except EmptyPage:
            current_page = paginator.page(paginator.num_pages)

        context = {
            'title': 'Новини та акції',
            'articles': current_page,
        }
        return render(request, 'blog/articles.html', context)


@method_decorator(cache_page(60 * 60 * 24), name='dispatch')
class ArticleView(View):
    def get(self, request, slug):
        try:
            art = Articles.objects.get(slug=slug)
        except Articles.DoesNotExist:
            raise Http404("Стаття не знайдена")

        context = {
            'title': art.title,
            'article': art,
        }
        return render(request, 'blog/article.html', context=context)
