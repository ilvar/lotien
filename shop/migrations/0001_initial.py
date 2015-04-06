# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u044f',
                'verbose_name_plural': '\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('price', models.PositiveIntegerField(verbose_name='\u0426\u0435\u043d\u0430')),
                ('baby', models.BooleanField(default=False, verbose_name='\u0414\u0435\u0442\u043a\u0430')),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'', verbose_name='\u0424\u043e\u0442\u043e')),
                ('collection', models.ForeignKey(to='shop.Collection')),
            ],
            options={
                'verbose_name': '\u0426\u0432\u0435\u0442\u043e\u043a',
                'verbose_name_plural': '\u0426\u0432\u0435\u0442\u044b',
            },
        ),
    ]
