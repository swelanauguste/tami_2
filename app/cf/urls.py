from django.contrib import admin
from django.urls import path, include

# from users.views import StaffCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("customers.urls")),
    path("users/", include("users.urls")),
    path("accounts/", include("allauth.urls")),
]
