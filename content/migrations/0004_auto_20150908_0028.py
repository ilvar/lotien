# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_sliderimage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='image_url',
            field=models.CharField(max_length=255, null=True, verbose_name='URL \u0444\u043e\u0442\u043e', blank=True),
        ),
    ]
