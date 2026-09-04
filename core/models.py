from django.db import models

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])

class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    from_account = models.ForeignKey(Account, related_name='transfers_from', on_delete=models.CASCADE)
    to_account = models.ForeignKey(Account, related_name='transfers_to', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    operation_key = models.CharField(max_length=100, unique=True)