# coding=utf-8
import json
import urllib
import StringIO
from PIL import Image

from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.management import BaseCommand
import os

from shop.models import Collection, Flower


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = json.load(open('sws.js'))
        slider = filter(lambda d: d['type'] == 'portfolio', data)[0]
        for d in data:
            if d['type'] != 'product_list' or d['page'] != u'Коллекции':
                continue

            collection_name = d['data']['block_title']
            collection, _ = Collection.objects.get_or_create(name=collection_name)
            for i in d['data']['items']:
                try:
                    Flower.objects.get(
                        collection=collection,
                        name=i['title'],
                    )
                except Flower.DoesNotExist:
                    try:
                        price = [int(s) for s in i['price'].split() if s.isdigit()][0]
                    except IndexError:
                        price = 0
                    flower = Flower(
                        collection=collection,
                        name=i['title'],
                        description=i['description'],
                        price=price,
                        baby=u'детка' in i['price'].lower(),
                    )

                    img_url = i['img']['full']
                    fname = os.path.basename(img_url)
                    f = urllib.urlopen(img_url)
                    io = StringIO.StringIO()
                    im = Image.open(f)
                    im = im.convert('RGB')
                    im.save(io, "JPEG")

                    flower.photo.save(fname + '.jpg', ContentFile(io.getvalue()))

                print 'Finished', i['title']
