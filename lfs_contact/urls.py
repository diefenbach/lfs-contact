# django imports
from django.conf.urls import patterns, url

urlpatterns = patterns('lfs_contact.views',
    url(r'^contact$', "contact_form", name='lfs_contact_form'),
    url(r'^contact-form-sent/$', "contact_form_sent", name='lfs_contact_form_sent'),
)
