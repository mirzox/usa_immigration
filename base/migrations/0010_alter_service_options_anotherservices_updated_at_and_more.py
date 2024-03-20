# Generated by Django 4.1 on 2024-03-20 08:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_anotherservices_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('created_at',), 'verbose_name': 'Check Form', 'verbose_name_plural': 'Check Forms'},
        ),
        migrations.AddField(
            model_name='anotherservices',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, serialize=False, verbose_name='Updated at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familyservices',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, serialize=False, verbose_name='Updated at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, serialize=False, verbose_name='Updated at'),
            preserve_default=False,
        ),
    ]