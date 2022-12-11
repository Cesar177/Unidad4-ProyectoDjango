from django.db import models

# Create your models here.

class IpDeClientes(models.Model):
    ip_client = models.CharField(max_length=100, default='0.0.0.0')

    class Meta:
        db_table = "ip_address"
