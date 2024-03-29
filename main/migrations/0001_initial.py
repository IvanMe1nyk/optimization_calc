# Generated by Django 4.0.4 on 2023-03-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetGold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('func', models.TextField(verbose_name='Функція')),
                ('left', models.FloatField(verbose_name='Ліва межа')),
                ('right', models.FloatField(verbose_name='Права межа')),
                ('exp', models.FloatField(verbose_name='Похибка')),
                ('dir', models.TextField(max_length=3, verbose_name='Напрямок оптимізації')),
            ],
        ),
    ]
