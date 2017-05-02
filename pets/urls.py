from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^species/(?P<species_id>[0-9]+)/$', views.species, name='species'),
    url(r'^ability/(?P<ability_id>[0-9]+)/$', views.ability, name='ability'),
]