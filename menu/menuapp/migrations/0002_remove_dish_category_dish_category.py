# Generated by Django 4.0.5 on 2022-06-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='category',
        ),
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.ManyToManyField(to='menuapp.category', verbose_name='Категории'),
        ),
    ]
