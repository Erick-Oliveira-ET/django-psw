from django.forms import ModelForm

from .models import Bill, BillPayment

class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = [
            "title",
            "category",
            "description",
            "value",
            "due_at",
        ]

class BillPaymentForm(ModelForm):
    class Meta:
        model = BillPayment
        fields = [
            "bill",
            "paid_at", 
        ]