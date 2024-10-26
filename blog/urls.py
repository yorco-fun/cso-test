from django.urls import path
from blog.views import BlogView, ArticleView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('article/<slug:slug>/', ArticleView.as_view(), name='article'),
]
