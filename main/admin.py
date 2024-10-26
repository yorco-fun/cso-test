from django.contrib import admin

from main.models import Main, FAQ, Vacancy

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Main)
admin.site.register(FAQ)
