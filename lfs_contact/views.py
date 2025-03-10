from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext as _

from lfs.catalog.models import Product
import lfs.customer.utils
from lfs_contact.forms import ContactForm
from lfs_contact.utils import send_contact_mail
from lfs.core.utils import import_symbol


def contact_form(request, template_name="lfs/contact/contact_form.html"):
    """Displays the contact form of LFS."""
    if getattr(settings, "LFS_CONTACT_FORM", None):
        contact_form = import_symbol(settings.LFS_CONTACT_FORM)
    else:
        contact_form = ContactForm

    if request.method == "POST":
        form = contact_form(data=request.POST)
        if form.is_valid():
            send_contact_mail(request, form)
            return HttpResponseRedirect(reverse("lfs_contact_form_sent"))
    else:
        customer = lfs.customer.utils.get_customer(request)
        product_id = request.GET.get("product_id", None)
        subject = ""
        try:
            name = customer.address.firstname + " " + customer.address.lastname
            email = customer.address.email
        except AttributeError:
            name = ""
            email = ""

        if product_id:
            try:
                product = Product.objects.get(pk=product_id, active=True)
            except Product.DoesNotExist:
                pass
            else:
                sku = product.get_sku()
                if sku:
                    sku = " (%s)" % sku
                subject = _("Availability of '%(product_name)s'%(sku)s") % dict(
                    product_name=product.get_name(), sku=sku
                )

        form = contact_form(initial={"name": name, "email": email, "subject": subject})

    return render(
        request,
        template_name,
        {
            "form": form,
        },
    )


def contact_form_sent(request, template_name="lfs/contact/contact_form_sent.html"):
    """Displays the page after the the contact form has been sent."""
    return render(request, template_name, {})
