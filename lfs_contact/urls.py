from django.conf.urls import url
import views

urlpatterns = [
    url(r'^contact/$', views.contact_form, name='lfs_contact_form'),
    url(r'^contact-form-sent/$', views.contact_form_sent, name='lfs_contact_form_sent'),
]
