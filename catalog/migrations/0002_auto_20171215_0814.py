# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='weight_override',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='weight_override',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, related_name='product_variants', to='catalog.ProductWeight'),
            preserve_default=False,
        ),
    ]
