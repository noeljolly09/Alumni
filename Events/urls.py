from django.urls import path
from . import views

urlpatterns = [
    path('',views.allEvents,name="allevents"),
    path('addevent', views.addEvents, name='addevent'),


]
