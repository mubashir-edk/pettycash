from django.db import models
import uuid
from django.utils.timezone import now as current_date

# Create your models here.
class Category(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    category = models.CharField(max_length=100)
    general_ledger_code = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.category

class PettyCash(models.Model):
    
    CASH_FLOW = (
        ('Cash In', 'Cash In'),
        ('Cash Out', 'Cash Out'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    voucher_code = models.CharField(max_length=150, blank=True, unique=True)
    to_or_from = models.CharField(max_length=200)
    created_date = models.DateField(default=current_date)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cash_flow = models.CharField(max_length=50, choices=CASH_FLOW)
    amount = models.FloatField()
    description = models.CharField(max_length=1200)
    image = models.ImageField(blank=True, null=True, upload_to="voucher_signature/")
    
    def __str__(self):
        return self.voucher_code
    
class FederalBank(models.Model):
    
    CASH_FLOW = (
        ('Cash In', 'Cash In'),
        ('Cash Out', 'Cash Out'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    voucher_code = models.CharField(max_length=150, blank=True, unique=True)
    to_or_from = models.CharField(max_length=200)
    created_date = models.DateField(default=current_date)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cash_flow = models.CharField(max_length=50, choices=CASH_FLOW)
    amount = models.FloatField()
    description = models.CharField(max_length=1200)
    image = models.ImageField(blank=True, null=True, upload_to="voucher_signature/")
    
    def __str__(self):
        return self.voucher_code
    
class SBIBank(models.Model):
    
    CASH_FLOW = (
        ('Cash In', 'Cash In'),
        ('Cash Out', 'Cash Out'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    voucher_code = models.CharField(max_length=150, blank=True, unique=True)
    to_or_from = models.CharField(max_length=200)
    created_date = models.DateField(default=current_date)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cash_flow = models.CharField(max_length=50, choices=CASH_FLOW)
    amount = models.FloatField()
    description = models.CharField(max_length=1200)
    image = models.ImageField(blank=True, null=True, upload_to="voucher_signature/")
    
    def __str__(self):
        return self.voucher_code
    
class VoucherCodeStore(models.Model):
    
    voucher_code = models.CharField(max_length=200)
    
    def __str__(self):
        return self.voucher_code
    
class OpeningBalance(models.Model):
    
    TYPE = (
        ('PettyCash', 'PettyCash'),
        ('Federal Bank', 'Federal Bank'),
        ('SBI Bank', 'SBI Bank'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    opening_balance = models.DecimalField(max_digits=50, decimal_places=2)
    opening_balance_of = models.CharField(max_length=50, choices=TYPE)
    opening_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.opening_date)