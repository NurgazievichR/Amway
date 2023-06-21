from django.contrib import admin

from apps.main.models import Main, Consultation


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
