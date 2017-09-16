# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robo', '0007_auto_20170729_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='robocomprado',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Aprovado'), (2, 'Cancelado'), (0, 'Pendente')], default=0, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='robocomprado',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Aprovado'), (2, 'Cancelado'), (0, 'Pendente')], default=0, verbose_name='Situacao'),
        ),
    ]