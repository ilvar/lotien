from django.db import models

import sirtrevor.fields


class Page(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = sirtrevor.fields.SirTrevorField()

    def __unicode__(self):
        return self.title
