from django.urls import path

from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='hello_django'),
    path('template1', views.call_template, name='call_template'),
]