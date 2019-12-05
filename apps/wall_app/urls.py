from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wall),
    url(r'^/messages$', views.messages),
    url(r'^/comments$', views.comments),
    url(r'^/destroy$', views.destroy),
]