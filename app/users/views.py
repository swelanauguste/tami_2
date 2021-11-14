from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView

from .forms import StaffCreateForm
from .models import User

# from django.contrib.auth.forms import UserCreationForm


class MyLoginView():
    def get_success_url(self):
        # url = self.get_redirect_url()
        return reverse(
            "users:user-detail",
            kwargs={"pk": self.request.user.pk}
        )


class StaffCreateView(CreateView):
    template_name = "users/staffcreate_form.html"
    form_class = StaffCreateForm

    def get_success_url(self):
        return reverse("account_login")


class UserDetailView(DetailView):
    model = User
    

def user_login_redirect(request):
    return redirect('users:user-detail', pk=request.user.pk)
