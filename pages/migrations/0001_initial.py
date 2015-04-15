# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sirtrevor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', sirtrevor.fields.SirTrevorField()),
            ],
        ),
    ]
