from utils.forms import CaptchaForm


def captcha_form(request, *args, **kwargs):
    cf = CaptchaForm()
    return {
        'captcha_form': cf,
    }