from django.urls import path
from . import views


app_name = 'dashboard'


urlpatterns = [
    path("", views.index, name="index"),
    path("data-tissue/", views.read_data_tissue, name="tissue_sensor_data"),
    path("data-smell/", views.read_data_smell, name="smell_sensor_data"),
    path("data-soup/", views.read_data_soup, name="soup_sensor_data"),
    path("data-show/", views.show_data, name="sensor_data_raw"),

]
