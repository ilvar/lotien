# coding=utf-8
from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField


class Collection(models.Model):
    name = models.CharField(u'Название', max_length=255)

    class Meta:
        verbose_name = u'Коллекция'
        verbose_name_plural = u'Коллекции'


class Flower(models.Model):
    collection = models.ForeignKey(Collection)
    name = models.CharField(u'Название', max_length=255)
    description = models.TextField(u'Описание')
    price = models.PositiveIntegerField(u'Цена')
    baby = models.BooleanField(u'Детка', blank=True, default=False)
    photo = ThumbnailerImageField(u'Фото')

    class Meta:
        verbose_name = u'Цветок'
        verbose_name_plural = u'Цветы'

    def __unicode__(self):
        return self.name
