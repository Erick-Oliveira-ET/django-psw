from django.db import models
from datetime import datetime
from django.db.models import Sum

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    essential = models.BooleanField(default=False)
    planning_value = models.FloatField(default=0)

    def __str__(self):
        return self.category
    
    def total_spending(self):
        from statement.models import Values
        values = Values.objects.filter(category__id = self.id).filter(date__month =datetime.now().month).aggregate(Sum("value"))
        return values["value__sum"] if values["value__sum"] else 0

    def calc_percent_spending_per_category(self):
        try:
            return (self.total_spending()*100)/self.planning_value
        except ZeroDivisionError:
            return 0
    
class Account(models.Model):
    bank_choices = (
        ('NU', 'Nubank'),
        ('CE', "Caixa Economica")
    )

    type_choices = (('pp', 'Physical Person',), ('jp', 'Juridical Person'))

    nickname = models.CharField(max_length=50)
    bank = models.CharField(max_length=2, choices=bank_choices)
    bank_type = models.CharField(max_length=2, choices=type_choices)
    value = models.IntegerField()
    icon = models.ImageField(upload_to="icons")

    def __str__(self):
        return self.nickname
    