from django import forms
from django.forms import HiddenInput
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    """Simple contact form for LFS."""

    name = forms.CharField(label=_("Name"))
    email = forms.EmailField(label=_("E-Mail"))
    subject = forms.CharField(label=_("Subject"), widget=HiddenInput, required=False)
    message = forms.CharField(label=_("Message"), widget=forms.Textarea())
