from django.db import models
from user_profile.models import Category, Account

# Create your models here.
class Values(models.Model):
    choice_type = (
        ('I', 'In'),
        ('O', 'Out')
    )
    
    value = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=1, choices=choice_type)

    def __str__(self):
        return self.description