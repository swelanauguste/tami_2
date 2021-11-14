from django.db import models
from users.models import User


class CustomerAddress(models.Model):
    """
    Model for Customer Address
    """
    user = models.ForeignKey(User, related_name="customer_addresses", on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.username + ", address"
