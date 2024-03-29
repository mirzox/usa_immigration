# Generated by Django 4.1 on 2024-02-21 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('tax', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='base.service')),
            ],
            options={
                'verbose_name': 'Another Service',
                'verbose_name_plural': 'Another Services',
            },
        ),
    ]
