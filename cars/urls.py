from django.urls import path
from . import views

urlpatterns = [
    path('create-car', views.create_car, name="create_car"),
    path('car-list',views.car_list, name="car_list"),
    path('edit-car/<slug:slug>', views.edit_car, name="edit_car"),
    path('delete-car/<slug:slug>', views.delete_car, name="delete_car"),
    path('upload-image', views.upload, name="upload_image"),
    path('search', views.search_by_owner, name='search_by_owner'),
   ]