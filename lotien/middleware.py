from django.conf import settings
from django.shortcuts import redirect


class SslOffMiddleware:
    def process_request(self, request):
        if request.is_secure() and not settings.DEBUG:
            return redirect('http://lotien.ru%s' % request.path)