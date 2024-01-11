from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^contact/$', views.contact_form, name='lfs_contact_form'),
    re_path(r'^contact-form-sent/$', views.contact_form_sent, name='lfs_contact_form_sent'),
]
