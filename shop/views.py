from django.views.generic import TemplateView

from content.models import SliderImage


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super(HomeView, self).get_context_data(**kwargs)
        data.update(
            slider_photos=SliderImage.objects.all().order_by('?')
        )
        return data


home = HomeView.as_view()
