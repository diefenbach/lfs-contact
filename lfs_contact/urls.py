# django imports
from django.conf.urls.defaults import *

urlpatterns = patterns('lfs_contact.views',
    url(r'^contact$', "contact_form", name='lfs_contact_form'),
    url(r'^contact-form-sent/$', "contact_form_sent", name='lfs_contact_form_sent'),
)
