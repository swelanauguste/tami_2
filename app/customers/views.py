from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from users.models import User
from .models import CustomerAddress


class MapServiceView(TemplateView):
    """
    View for the map service page
    """

    template_name = "map_service.html"


class CustomerAddressListView(ListView):
    model = CustomerAddress


class CustomerDetailView(DetailView):
    model = CustomerAddress
    template_name = "customers/customer_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['number'] = random.randrange(1, 100)
    #     return context
