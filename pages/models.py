from django.db import models

import sirtrevor.fields


class Page(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    show_on_main = models.BooleanField(default=False)
    content = sirtrevor.fields.SirTrevorField()

    def __unicode__(self):
        return self.title
