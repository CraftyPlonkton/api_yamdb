# Generated by Django 2.2.16 on 2022-05-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220516_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=None, null=True, verbose_name='Рейтинг'),
        ),
    ]
