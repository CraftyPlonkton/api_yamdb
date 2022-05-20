# Generated by Django 2.2.16 on 2022-05-19 11:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20220517_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Допустимы значения от 1 до 10'), django.core.validators.MaxValueValidator(10, 'Допустимы значения от 1 до 10')], verbose_name='Рейтинг'),
        ),
    ]
