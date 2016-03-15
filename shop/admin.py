from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from shop.models import Collection, Flower

admin.site.register(Collection)
admin.site.register(Flower, MarkdownModelAdmin)
