# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='not_available',
            field=models.TextField(default=b'', verbose_name='\u041d\u0435\u0442 \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438 (\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435)'),
        ),
    ]
