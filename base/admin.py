from django.contrib import admin
from django.db import models
from django import forms

from .models import Service, AnotherServices, FamilyServices


class CharFieldForm(forms.ModelForm):
    class Meta:
        widgets = {'title_en': forms.TextInput(attrs={'size': 80})}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_en', 'text_preview', 'price_en', 'created_at', 'updated_at']
    search_fields = ['title_en', 'title_ru', 'text_en', 'text_ru', 'price_en', 'price_ru']
    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size': '120'})}
    }

@admin.register(AnotherServices)
class AnotherServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_en', 'text_preview', 'price_en', 'created_at', 'updated_at']
    search_fields = ['title_description_en', 'title_description_ru', 'price_en', 'price_ru']
    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size': '120'})}
    }
    # autocomplete_fields = ['service_id']


@admin.register(FamilyServices)
class FamilyServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_en', 'text_preview', 'price_en', 'created_at', 'updated_at']
    search_fields = ['title_description_en', 'title_description_ru', 'price_en', 'price_ru']
    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size': '120'})}
    }

