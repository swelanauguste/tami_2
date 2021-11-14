from django.urls import path

from . import views

app_name = "customers"

urlpatterns = [
    path("", views.MapServiceView.as_view(), name="landing"),
    path("<int:pk>", views.CustomerDetailView.as_view(), name="customer-detail"),
]
