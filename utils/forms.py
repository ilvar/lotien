# coding=utf-8
from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class CaptchaForm(forms.Form):
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'placeholder': u'Результат цифрами'}))