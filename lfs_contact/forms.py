from django import forms
from django.forms import HiddenInput
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    """Simple contact form for LFS.
    """
    name = forms.CharField(label=_(u'Name'))
    email = forms.EmailField(label=_(u'E-Mail'))
    subject = forms.CharField(label=_(u'Subject'), widget=HiddenInput, required=False)
    message = forms.CharField(label=_(u'Message'), widget=forms.Textarea())
