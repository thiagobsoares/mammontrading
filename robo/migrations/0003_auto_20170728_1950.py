# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robo', '0002_auto_20170728_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robo',
            name='imagem',
            field=models.ImageField(upload_to='imagens', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='robocomprado',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Pendente'), (2, 'Cancelado'), (1, 'Aprovado')], default=0, verbose_name='Situacao'),
        ),
    ]
