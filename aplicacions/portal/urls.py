from django.conf.urls import url

from . import views

app_name = "portal"
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^comanda$', views.comanda, name='comanda'),
]