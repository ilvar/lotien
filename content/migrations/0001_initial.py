# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(help_text='\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c, \u0435\u0441\u043b\u0438 \u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d URL', upload_to=b'', verbose_name='\u0424\u0430\u0439\u043b \u0444\u043e\u0442\u043e')),
                ('image_url', models.URLField(verbose_name='URL \u0444\u043e\u0442\u043e')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e \u0434\u043b\u044f \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e \u0434\u043b\u044f \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430',
            },
        ),
    ]
