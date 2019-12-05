from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validate$', views.validate),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^ajax/validate_email/$', views.validate_email, name='validate_email'),
]
