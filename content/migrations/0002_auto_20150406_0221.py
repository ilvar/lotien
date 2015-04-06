# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(help_text='\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c, \u0435\u0441\u043b\u0438 \u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d URL', upload_to=b'', verbose_name='\u0424\u0430\u0439\u043b \u0444\u043e\u0442\u043e', blank=True),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='image_url',
            field=models.CharField(max_length=255, verbose_name='URL \u0444\u043e\u0442\u043e'),
        ),
    ]
