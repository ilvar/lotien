import json

from django.core.exceptions import MultipleObjectsReturned
from django.core.management import BaseCommand

from content.models import SliderImage


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = json.load(open('sws.js'))
        slider = filter(lambda d: d['type'] == 'portfolio', data)[0]
        for i in slider['data']['items']:
            url = i['img']['full']
            print url
            try:
                si, created = SliderImage.objects.get_or_create(image_url=url)
                if not created and not si.image:
                    si.save()
            except MultipleObjectsReturned:
                pass
