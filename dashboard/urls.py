from django.urls import path
from . import views


app_name = 'dashboard'


urlpatterns = [
    path("", views.index, name="index"),
    path("data-tissue/", views.read_data_tissue, name="tissue_sensor_data"),
    path("data-smell/", views.read_data_smell, name="smell_sensor_data"),
    path("data-soup/", views.read_data_soup, name="soup_sensor_data"),
    path("data-show/", views.show_data, name="sensor_data_raw"),
    path("api/data-tissue/", views.TissuesensorAPIView.as_view(), name="tissue_api"),
    path("api/data-smell/", views.SmellsensorAPIView.as_view(), name="smell_api"),
    path("api/data-soap/", views.SoapsensorAPIView.as_view(), name="smell_api"),
    path("update-data/", views.update_data, name="update_data"),



]
