from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('search', views.search, name="search"),
    path('create-measurement', views.create_measurement, name="create_measurement"),
    path('measurement-list', views.measurement_list, name="measurement_list"),
    path('measurement-edit/<slug:slug>', views.measurement_edit, name="measurement_edit"),
    path('measurement-delete/<slug:slug>', views.measurement_delete, name="measurement_delete"),
    path('upload', views.upload, name="upload"),
    path('<slug:slug>',views.details, name="measurement_details"),
    path('car/<slug:slug>',views.getMeasurementsByCar, name = 'measurements_by_car'),
]