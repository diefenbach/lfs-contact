# python imports
import datetime

# django imports
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

# lfs imports
import lfs.core.utils


def send_contact_mail(request, form, template="lfs/mail/contact_mail.html"):
    """Sends an internal mail after a customer as submit the standard contact
    form.
    """
    shop = lfs.core.utils.get_default_shop()
    subject = _(u"New mail from %(shop)s" % {"shop": shop.name})
    from_email = request.POST.get("email")
    to = shop.get_notification_emails()
    bcc = []

    fields = []
    for field_name, field in form.fields.items():
        fields.append({
            "label": _(field.label.title()),
            "value": form.cleaned_data.get(field_name)
        })

    text = render_to_string(template, RequestContext(request, {
        "date": datetime.datetime.now(),
        "shop": shop,
        "fields": fields,
    }))

    mail = EmailMultiAlternatives(subject=subject, body="", from_email=from_email, to=to, bcc=bcc)
    mail.attach_alternative(text, "text/html")

    mail.send()
