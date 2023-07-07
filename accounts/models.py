from django.db import models
from user_profile.models import Category

# Create your models here.
class Bill(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    value = models.FloatField()
    payday = models.IntegerField()
    
    def __str__(self):
        return self.title

class Payment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    pay_date = models.DateField()