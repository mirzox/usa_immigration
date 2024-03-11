from django.db import models

from ckeditor.fields import RichTextField


class Service(models.Model):
    title_en = models.CharField(
        max_length=255,
        verbose_name='Title in English'
    )
    text_en = models.TextField(
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
    text_ru = models.TextField(
        verbose_name='Description in Russian'
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

    @property
    def text_preview(self):
        if len(self.text_en) > 150:
            return f"{self.text_en[:150]} ..."
        return self.text_en

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

    class Meta:
        verbose_name = 'Family Service'
        verbose_name_plural = 'Family Services'
