from django.urls import path

from . import views

app_name = "users"


urlpatterns = [
    path("<int:pk>", views.UserDetailView.as_view(), name="user-detail"),
    path("add/staff", views.StaffCreateView.as_view(), name="staff-create"),
    path("login-redirect", views.user_login_redirect, name="login-redirect"),
]
