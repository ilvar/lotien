# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20150406_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c'),
        ),
    ]
