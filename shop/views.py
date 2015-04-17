# coding=utf-8
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
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
            collections=Collection.objects.all().order_by('name'),
        )
        return data

home = HomeView.as_view()


class CollectionView(ListView):
    template_name = 'collection.html'
    context_object_name = 'flowers'

    def get_queryset(self):
        return Flower.objects.filter(collection__pk=self.kwargs['pk']).order_by('name')

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

        fl = self.get_object()

        self.request.session['order'].append({
            'pk': fl.pk,
            'count': 1,
        })
        self.request.session.save()

        messages.success(self.request, u'Товар добавлен в корзину. Если больше ничего не хотите '
                                       u'<a href="/#collections">выбрать</a>, можете '
                                       u'<a href="/cart/">оформить заказ.</a>')

        url = reverse('collection', args=[fl.collection.pk])
        return redirect(url + '#flower_%s' % fl.pk)

flower = FlowerView.as_view()


class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        data = super(CartView, self).get_context_data(**kwargs)
        order = self.request.session['order']
        for f in order:
            f['flower'] = Flower.objects.get(pk=f['pk'])
        data['order'] = order
        data['total'] = sum([f['flower'].price * f['count'] for f in order], 0)
        return data

    def post(self, *args, **kwargs):
        if self.request.POST.get('update'):
            for f in self.request.session['order']:
                key = 'count_%s' % f['pk']
                value = self.request.POST.get(key)
                if value:
                    f['count'] = int(value)

            self.request.session.save()
            messages.success(self.request, u'Ваш заказ успешно пересчитан')
            return redirect('.')

        if self.request.POST.get('checkout'):
            msg = [u'Новый заказ:', u'']

            order = self.request.session['order']
            total = 0
            for item in order:
                fl = Flower.objects.get(pk=item['pk'])
                total += fl.price * item['count']

                msg.append(u'%s: %s (%s шт)' % (fl.name, fl.price, item['count']))

            msg.append(u'')

            msg.append(u'Итого: %s' % total)

            msg.append(u'')

            msg.append(u'Имя: %s' % self.request.POST['name'])
            msg.append(u'Email: %s' % self.request.POST['email'])
            msg.append(u'Телефон: %s' % self.request.POST['phone'])
            msg.append(u'Адрес:\n %s' % self.request.POST['address'])

            emails = ['fuchsiairk@mail.ru', 'info@lotien.ru']
            send_mail(u'Новый заказ', '\n'.join(msg), settings.DEFAULT_FROM_EMAIL, emails)

            del self.request.session['order']
            messages.success(self.request, u'Ваш заказ отправлен, я скоро с Вами свяжусь')
            return redirect('/')

        return redirect('.')

cart = CartView.as_view()
