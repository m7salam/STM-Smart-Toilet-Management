from django.urls import path
from . import views


app_name = 'dashboard'


urlpatterns = [
    path("", views.index, name="index"),
    path("data/", views.read_data, name="sensor_data"),

]
