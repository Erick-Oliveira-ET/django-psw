from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants

from datetime import datetime

from user_profile.models import Category
from .forms import BillForm, BillPaymentForm
from .models import Bill, BillPayment

def view_bill(req):
    CURRENT_MONTH = datetime.now().month
    CURRENT_DAY = datetime.now().day

    bills = Bill.objects.all()
    paid_bills = BillPayment.objects.filter(paid_at__month=CURRENT_MONTH).values('bill')
    overdue_bills = bills.filter(due_at__lt=CURRENT_DAY).exclude(id__in=paid_bills)
    soon_dued_bills = bills.filter(due_at__lte = CURRENT_DAY + 5).filter(due_at__gte=CURRENT_DAY).exclude(id__in=paid_bills)
    remaining_bills = bills.exclude(id__in=paid_bills).exclude(id__in=overdue_bills).exclude(id__in=soon_dued_bills)
    
    return render(req, 'view_bill.html', {
        "overdue_bills": overdue_bills,
        "soon_dued_bills": soon_dued_bills,
        "remaining_bills": remaining_bills,
    })



def create_bill(req):
    if req.method == "GET":
        categories = Category.objects.all()
        return render(req, 'create_bill.html', {'categories': categories})
    else:
        details = BillForm(req.POST)

        if details.is_valid(): 
            account = details.save(commit = False)

            account.save() 

            messages.add_message(req, constants.SUCCESS, 'Bill created successfully!')

            return redirect("view_bill") 
                
        else:
            for error in details.errors:
                messages.add_message(req, constants.ERROR, f'Field "{error}": {details.errors[error][0]}')
            return redirect("create_bill") 
        
def pay_bill(req, id):
    details = BillPaymentForm({"bill":id,"paid_at":datetime.now()})
    
    if details.is_valid(): 
        account = details.save(commit = False)

        account.save() 

        messages.add_message(req, constants.SUCCESS, 'Bill paid successfully!')

        return redirect("view_bill") 
            
    else:
        for error in details.errors:
            messages.add_message(req, constants.ERROR, f'Field "{error}": {details.errors[error][0]}')
        return redirect("create_bill") 