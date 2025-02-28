from django.urls import path

from . import views

urlpatterns = [
    path("contact", views.contact_form, name="lfs_contact_form"),
    path("contact-form-sent", views.contact_form_sent, name="lfs_contact_form_sent"),
]
