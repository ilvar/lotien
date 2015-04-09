# coding=utf-8
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
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

    def post(self, *args, **kwargs):
        if 'order' not in self.request.session:
            self.request.session['order'] = []

        self.request.session['order'].append({
            'pk': self.kwargs['pk'],
            'count': 1,
        })

        return redirect('/cart/')

flower = FlowerView.as_view()


class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        data = super(CartView, self).get_context_data(**kwargs)
        order = self.request.session['order']
        for f in order:
            f['flower'] = Flower.objects.get(pk=f['pk'])
        data['order'] = order
        data['total'] = sum([f['flower'].price for f in order], 0)
        return data

    def post(self, *args, **kwargs):
        msg = [u'Новый заказ:']

        msg.append(u'')

        order = self.request.session['order']
        total = 0
        for f in order:
            flower = Flower.objects.get(pk=f['pk'])
            total += flower.price

            msg.append(u'%s: %s' % (flower.name, f['count']))

        msg.append(u'')

        msg.append(u'Итого: %s' % total)

        msg.append(u'')

        msg.append(u'Имя: %s' % self.request.POST['name'])
        msg.append(u'Email: %s' % self.request.POST['email'])
        msg.append(u'Телефон: %s' % self.request.POST['phone'])

        send_mail(u'Новый заказ', '\n'.join(msg), settings.DEFAULT_FROM_EMAIL, ['fuchsiairk@mail.ru'])

        del self.request.session['order']
        messages.success(self.request, u'Ваш заказ отправлен, я скоро с Вами свяжусь')
        return redirect('/')

cart = CartView.as_view()
