from django.db import models

# Create your models here.
class MVRS_Category(models.Model):
    MVRS_cat_name = models.CharField(max_length=100)
    MVRS_cat_description =models.TextField()
class MVRS_Cars(models.Model):
    MVRS_cat_name = models.CharField(max_length=100)
    MVRS_cat_description =models.TextField()
class Booking(models.Model):
    client_name = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=10)
    client_email =models.EmailField()
    select_vehicle = models.CharField(max_length=255)
    period_from = models.DateField()
    period_to = models.DateField()
class contact(models.Model):
    client_id  = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=10)
    client_problem = models.CharField(max_length=255)
    raised_on = models.DateField(auto_now=True)
    def __str__(self):
        return f"Help Message for phone number {self.client_phone}"
