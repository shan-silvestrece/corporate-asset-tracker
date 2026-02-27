from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now  

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class User(AbstractUser):
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )

class Asset(models.Model):
    name = models.CharField(max_length=200)
    asset_type = models.CharField(max_length=100, default="Hardware") 
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    repair_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class MaintenanceLog(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='maintenance_logs')
    service_date = models.DateField(default=now) 
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.asset.name} Repair - {self.service_date}"
        