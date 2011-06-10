# django imports
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

# lfs imports
import lfs.customer.utils
from lfs_contact.forms import ContactForm
from lfs_contact.utils import send_contact_mail


def contact_form(request, template_name="lfs/contact/contact_form.html"):
    """Displays the contact form of LFS.
    """
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            send_contact_mail(request, form)
            return HttpResponseRedirect(reverse("lfs_contact_form_sent"))
    else:
        customer = lfs.customer.utils.get_customer(request)

        try:
            name = customer.address.firstname + " " + customer.address.lastname
            email = customer.address.email
        except AttributeError:
            name = ""
            email = ""

        form = ContactForm(initial={"name": name, "email": email})

    return render_to_response(template_name, RequestContext(request, {
        "form": form,
    }))


def contact_form_sent(request, template_name="lfs/contact/contact_form_sent.html"):
    """Displays the page after the the contact form has been sent.
    """
    return render_to_response(template_name, RequestContext(request, {}))
