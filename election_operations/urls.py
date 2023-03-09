from django.urls import path
from . import views

urlpatterns = [
    path('polling_unit_result/', views.polling_unit_result, name="polling_result"),
    path('lga_result_from_pu/', views.lga_result_from_pu, name="lga_result_from_pu")
]