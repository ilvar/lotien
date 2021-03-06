# coding=utf-8
from django.db import models
from django_markdown.models import MarkdownField

from easy_thumbnails.fields import ThumbnailerImageField
from utils import thumbnail_storage


class Collection(models.Model):
    name = models.CharField(u'Название', max_length=255)
    not_available = models.TextField(u'Нет в наличии (сообщение)', default='')

    class Meta:
        verbose_name = u'Коллекция'
        verbose_name_plural = u'Коллекции'

    def __unicode__(self):
        return self.name


class Flower(models.Model):
    collection = models.ForeignKey(Collection)
    name = models.CharField(u'Название', max_length=255)
    description = MarkdownField(u'Описание')
    price = models.PositiveIntegerField(u'Цена')
    baby = models.BooleanField(u'Детка', blank=True, default=False)
    photo = ThumbnailerImageField(u'Фото', thumbnail_storage=thumbnail_storage)

    class Meta:
        verbose_name = u'Цветок'
        verbose_name_plural = u'Цветы'

    def __unicode__(self):
        return self.name

    @property
    def short_description(self):
        words = self.description.split()[:10]
        while len(words) and len(words[-1]) < 4:
            words = words[:-1]
        if not words:
            words = self.description.split()[:10]
        return ' '.join(words)

    @property
    def cover_height(self):
        w, h = self.photo.width, self.photo.height
        print w, h
        return int(960.0 / w * h)

import andablog.models
import pytils.translit

def update_slug(instance, **kwargs):
    if not instance.slug:
        andablog.models.Entry.objects.filter(pk=instance.pk).update(slug=pytils.translit.slugify(instance.title))

models.signals.post_save.connect(update_slug, sender=andablog.models.Entry)
