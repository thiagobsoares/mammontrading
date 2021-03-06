# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robo', '0004_auto_20170728_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robo',
            name='descricao',
            field=models.TextField(verbose_name='Descricao'),
        ),
        migrations.AlterField(
            model_name='robocomprado',
            name='status',
            field=models.IntegerField(blank=True, choices=[(2, 'Cancelado'), (1, 'Aprovado'), (0, 'Pendente')], default=0, verbose_name='Situacao'),
        ),
    ]
