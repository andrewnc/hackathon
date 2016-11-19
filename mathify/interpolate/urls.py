from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'landing/', views.landing_render, name='landing'),
    url(r'info/', views.getFormData, name='info'),

]