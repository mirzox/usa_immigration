import datetime

from django.utils.timezone import now
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField


class Service(models.Model):
    title_en = models.CharField(
        max_length=255,
        verbose_name='Title in English'
    )
    text_en = RichTextField(
        verbose_name='Description in English'
    )
    price_en = models.CharField(
        max_length=255,
        verbose_name='Price in English'
    )

    title_ru = models.CharField(
        max_length=255,
        verbose_name='Title in Russian'
    )
    text_ru = RichTextField(
        verbose_name='Description description in Russian'
    )
    price_ru = models.CharField(
        max_length=255,
        verbose_name='Price in Russian'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        serialize=False,
        verbose_name='Created at'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        serialize=False,
        verbose_name='Updated at'
    )

    @property
    def text_preview(self):
        if len(self.text_en) > 100:
            return f"{self.text_en[:100]} ...".replace('<p>&nbsp;</p>', '').replace('<p>', '').replace('</p>', '').replace('<strong>', '')
        return self.text_en.replace('<p>&nbsp;</p>', '').replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('<strong>', '')

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Check Form'
        verbose_name_plural = 'Check Forms'
        ordering = ('created_at', )


class AnotherServices(models.Model):
    title_en = models.CharField(
        max_length=255,
        verbose_name='Title in English'
     )
    title_description_en = models.TextField(
        verbose_name='Title description in English'
    )
    description_en = RichTextField(verbose_name='Description')
    price_en = models.CharField(
        max_length=255,
        verbose_name='Price in English'
    )
    tax_en = models.CharField(
        max_length=255,
        verbose_name='Tax in English'
    )

    title_ru = models.CharField(
        max_length=255,
        verbose_name='Title in Russian'
    )
    title_description_ru = models.TextField(
        verbose_name='Title description in Russian'
    )
    description_ru = RichTextField(verbose_name='Description')

    price_ru = models.CharField(
        max_length=255,
        verbose_name='Price in Russian'
    )
    tax_ru = models.CharField(
        max_length=255,
        verbose_name='Tax in Russian'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        serialize=False,
        verbose_name='Created at'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        serialize=False,
        verbose_name='Updated at'
    )

    @property
    def text_preview(self):
        if len(self.description_en) > 100:
            return f"{self.description_en[:100]} ...".replace('<p>&nbsp;</p>', '').replace('<p>', '').replace('</p>', '').replace('<strong>', '')
        return self.description_en.replace('<p>&nbsp;</p>', '').replace('<p>', '').replace('</p>', '').replace('<strong>', '')
    class Meta:
        verbose_name = 'Another Service'
        verbose_name_plural = 'Another Services'


class FamilyServices(models.Model):
    title_en = models.CharField(
        max_length=255,
        verbose_name='Title in English'
    )
    title_description_en = models.TextField(
        verbose_name='Title description in English'
    )
    description_en = RichTextField(verbose_name='Description in English')
    price_en = models.CharField(
        max_length=255,
        verbose_name='Price in English'
    )
    tax_en = models.CharField(
        max_length=255,
        verbose_name='Tax in English'
    )

    title_ru = models.CharField(
        max_length=255,
        verbose_name='Title in Russian'
    )
    title_description_ru = models.TextField(
        verbose_name='Title description in Russian'
    )
    description_ru = RichTextField(verbose_name='Description description in Russian')
    price_ru = models.CharField(
        max_length=255,
        verbose_name='Price in Russian'
    )
    tax_ru = models.CharField(
        max_length=255,
        verbose_name='Tax in Russian'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        serialize=False,
        verbose_name='Created at'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        serialize=False,
        verbose_name='Updated at'
    )

    @property
    def text_preview(self):
        if len(self.description_en) > 100:
            return f"{self.description_en[:100]} ...".replace('<p>&nbsp;</p>', '').replace('<p>', '').replace('</p>', '').replace('<strong>', '')
        return self.description_en.replace('<p>&nbsp;</p>', '').replace('<p>', '').replace('</p>', '').replace('<strong>', '')

    class Meta:
        verbose_name = 'Family Service'
        verbose_name_plural = 'Family Services'


@receiver(post_save, sender=Service, dispatch_uid="update_check_form")
def update_check_form(sender, instance, created, **kwargs):
    if not created:
        Service.objects.filter(id=instance.id).update(updated_at=now())


@receiver(post_save, sender=AnotherServices, dispatch_uid="update_another_service")
def update_another_service(sender, instance, created, **kwargs):
    if not created:
        AnotherServices.objects.filter(id=instance.id).update(updated_at=now())


@receiver(post_save, sender=FamilyServices, dispatch_uid="update_family_service")
def update_family_service(sender, instance, created, **kwargs):
    if not created:
        FamilyServices.objects.filter(id=instance.id).update(updated_at=now())
