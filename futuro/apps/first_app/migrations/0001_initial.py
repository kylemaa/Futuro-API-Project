# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_shares', models.IntegerField()),
                ('profit', models.FloatField()),
                ('invested', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=20)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('sum_invested', models.FloatField()),
                ('sum_profit', models.FloatField()),
                ('my_basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Basket')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='my_stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Stock'),
        ),
    ]