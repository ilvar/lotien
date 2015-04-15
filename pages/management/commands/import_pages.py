# coding=utf-8
import json

from django.core.management import BaseCommand

import html2text
import pytils.translit

from pages.models import Page


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = json.load(open('sws.js'))

        texts = filter(lambda d: d['type'] == 'info', data)
        for t in texts:
            title = t['data']['title']
            text = t['data']['text']
            url = '/%s/' % pytils.translit.slugify(title)
            print url
            try:
                Page.objects.get(url=url)
            except Page.DoesNotExist:
                content = json.dumps({
                    "data": [{
                        "type": "text",
                        "data": {
                            "text": html2text.html2text(text)
                        }
                    }]
                })

                Page.objects.create(
                    title=title,
                    url=url,
                    content=content,
                )

        articles = filter(lambda d: d['type'] == 'articles', data)

        index_url = '/nachinayushim/'
        try:
            Page.objects.get(url=index_url)
        except Page.DoesNotExist:
            index_text = ''

            for a in articles:
                for a1 in a['data']['items']:
                    title = a1['title']
                    text = a1['text']
                    brief = a1['brief']
                    url = '/%s/' % pytils.translit.slugify(title)
                    print url

                    content = json.dumps({
                        "data": [{
                            "type": "text",
                            "data": {
                                "text": html2text.html2text(text)
                            }
                        }]
                    })

                    Page.objects.create(
                        title=title,
                        url=url,
                        content=content,
                    )

                    index_text += '# [%s](%s)\n\n%s\n\n' % (title, url, brief)

            content = json.dumps({
                "data": [{
                    "type": "text",
                    "data": {
                        "text": index_text
                    }
                }]
            })

            Page.objects.create(
                title=u'Начинающим',
                url=index_url,
                content=content,
            )

