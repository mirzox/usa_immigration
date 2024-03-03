from django.contrib import admin

from .models import Service, AnotherServices, FamilyServices


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_en', 'text_preview', 'price_en', 'created_at']
    search_fields = ['title_en', 'title_ru', 'text_en', 'text_ru', 'price_en', 'price_ru']


@admin.register(AnotherServices)
class AnotherServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_en', 'price_en']
    # autocomplete_fields = ['service_id']


@admin.register(FamilyServices)
class FamilyServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_en', 'price_en']
