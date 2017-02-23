from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    """Simple contact form for LFS.
    """
    name = forms.CharField(label=_(u'Name'))
    email = forms.EmailField(label=_(u'E-Mail'))
    message = forms.CharField(label=_(u'Message'), widget=forms.Textarea())
