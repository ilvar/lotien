from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from pages.models import Page


class PageView(DetailView):
    template_name = 'page.html'
    context_object_name = 'page'

    def get_object(self, queryset=None):
        path = self.request.path.strip('/')
        page = get_object_or_404(Page, url='/%s/' % path)
        return page

page = PageView.as_view()
