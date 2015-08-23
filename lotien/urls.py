from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'shop.views.home', name='home'),
    url(r'^collection/(?P<pk>\d+)/$', 'shop.views.collection', name='collection'),
    url(r'^collection/(?P<collection_pk>\d+)/(?P<pk>\d+)/$', 'shop.views.flower', name='flower'),
    url(r'^cart/$', 'shop.views.cart', name='cart'),
    url(r'^contact/$', 'shop.views.contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sirtrevor/', include('sirtrevor.urls')),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^', 'pages.views.page', name='page'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)