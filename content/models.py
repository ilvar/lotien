# coding=utf-8
import os
import urllib
import StringIO

from PIL import Image
from django.conf import settings
from django.db import models
from django.core.files.base import ContentFile

from easy_thumbnails.fields import ThumbnailerImageField
from utils import thumbnail_storage


class SliderImage(models.Model):
    image = ThumbnailerImageField(u'Файл фото', help_text=u'Необходим, если не указан URL', blank=True,
                                  resize_source=dict(size=(960, 445), crop="smart", upscale=True),
                                  thumbnail_storage=thumbnail_storage)
    image_url = models.CharField(u'URL фото', max_length=255, blank=True, null=True)
    title = models.CharField(u'Подпись', max_length=255, null=True)

    class Meta:
        verbose_name = u'Фото для слайдера'
        verbose_name_plural = u'Фото для слайдера'

    @property
    def url(self):
        if self.image:
            return self.image.url
        else:
            return self.image_url

    def __unicode__(self):
        return os.path.basename(self.url)

    def save(self, *args, **kwargs):
        if not self.image and self.image_url:
            fname = os.path.basename(self.image_url)
            f = urllib.urlopen(self.image_url)
            io = StringIO.StringIO()
            im = Image.open(f)
            im.save(io, "JPEG")
            self.image.save(fname + '.jpg', ContentFile(io.getvalue()), save=False)

        return super(SliderImage, self).save(*args, **kwargs)
