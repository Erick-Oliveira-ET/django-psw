from django.db import models

from user_profile.models import Category

# Create your models here.
class Bill(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    value = models.FloatField()
    due_at = models.IntegerField()
    
    def __str__(self):
        return self.title

class BillPayment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    paid_at = models.DateField()