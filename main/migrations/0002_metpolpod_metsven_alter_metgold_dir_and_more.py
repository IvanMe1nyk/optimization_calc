# Generated by Django 4.0.4 on 2023-03-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetPolPod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('func', models.TextField()),
                ('left', models.FloatField()),
                ('right', models.FloatField()),
                ('exp', models.FloatField()),
                ('dir', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='MetSven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('func', models.TextField()),
                ('x', models.FloatField()),
                ('exp', models.FloatField()),
                ('dir', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='metgold',
            name='dir',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='metgold',
            name='exp',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='metgold',
            name='func',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='metgold',
            name='left',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='metgold',
            name='right',
            field=models.FloatField(),
        ),
    ]