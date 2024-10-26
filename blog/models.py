from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Категорія')
    slug = models.SlugField(max_length=100, unique=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name
     

class Articles(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique=True, null=True, verbose_name='URL')
    text = models.TextField(null=True, verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата публікації')
    image = models.ImageField(upload_to='blog', null=True, verbose_name='Зображення')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категорія')
    
    class Meta:
        db_table = 'article'
        verbose_name = 'Статтю'
        verbose_name_plural = 'Статті'
        ordering = ['-date']

    def __str__(self):
        return self.title