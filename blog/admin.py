from django.contrib import admin

from blog.models import Categories, Articles


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
