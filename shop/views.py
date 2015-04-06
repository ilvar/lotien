from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

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


class CollectionView(ListView):
    template_name = 'collection.html'
    context_object_name = 'flowers'

    def get_queryset(self):
        return Flower.objects.filter(collection__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        data = super(CollectionView, self).get_context_data(**kwargs)
        data.update(
            collection=get_object_or_404(Collection, pk=self.kwargs['pk'])
        )
        return data

collection = CollectionView.as_view()


class FlowerView(DetailView):
    template_name = 'flower.html'
    context_object_name = 'flower'

    def get_queryset(self):
        return Flower.objects.filter(collection__pk=self.kwargs['collection_pk'])

flower = FlowerView.as_view()
