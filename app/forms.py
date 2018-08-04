from django import forms

from django.contrib.auth.forms import AuthenticationForm
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'picture', 'text', )

class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget = ReCaptchaWidget(), label = '')

