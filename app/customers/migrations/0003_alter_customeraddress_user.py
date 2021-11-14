# Generated by Django 3.2.4 on 2021-11-14 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0002_alter_customeraddress_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_addresses', to=settings.AUTH_USER_MODEL),
        ),
    ]
