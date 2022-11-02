from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    STATUS = (
        ('Complete', 'Complete'),
        ('Pending', 'Pending'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    recipients_name = models.CharField(max_length=200, null=True)
    recipients_account_number = models.CharField(max_length=200, null=True)
    amount = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

