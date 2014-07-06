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

    # Add Sender header, because eg. Gmail don't like From header set to @gmail
    # but email not really sent by gmail servers.
    # If email is sent From: @gmail.com it generates the following message in our postfix
    # host gmail-smtp-in.l.google.com[74.125.136.26] said: 421-4.7.0 [xx.xx.xx.xx 15]
    # Our system has detected an unusual rate of 421-4.7.0 unsolicited mail
    # originating from your IP address. To protect our 421-4.7.0 users from
    # spam, mail sent from your IP address has been temporarily 421-4.7.0 rate
    # limited. Please visit 421-4.7.0 http://www.google.com/mail/help/bulk_mail.html
    # to review our Bulk 421 4.7.0 Email Senders Guidelines.
    headers = {
        'Sender': shop.from_email
    }

    mail = EmailMultiAlternatives(subject=subject, body="", from_email=from_email, to=to, bcc=bcc, headers=headers)
    mail.attach_alternative(text, "text/html")

    mail.send()
