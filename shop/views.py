from django.views.generic import TemplateView

from content.models import SliderImage
from shop.models import Flower, Collection


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super(HomeView, self).get_context_data(**kwargs)
        data.update(
            slider_photos=SliderImage.objects.all().order_by('?'),
            flowers=Flower.objects.all().order_by('?')[:3],
            collections=Collection.objects.all().order_by('id'),
        )
        return data


home = HomeView.as_view()
