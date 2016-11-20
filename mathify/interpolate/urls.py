from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.landing_render, name='landing'),
    url(r'submit/', views.index, name='index'),
    url(r'info/', views.getFormData, name='info'),

]