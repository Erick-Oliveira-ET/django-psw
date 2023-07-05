from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum

from .forms import CategoryForm, AccountForm
from .models import Account, Category

# Create your views here.
def home(req):
    return render(req, "home.html")

def manage(req):
    accounts = Account.objects.all()
    account_total_value = Account.objects.all().aggregate(Sum('value'))['value__sum']

    categories = Category.objects.all()

    return render(req, "manage.html", {"accounts": accounts, "account_total_value": account_total_value, "categories": categories})

def create_account(req):
    if req.method != 'POST':
        return HttpResponse(status=405)
    
    details = AccountForm(req.POST, req.FILES)

    if details.is_valid(): 
        account = details.save(commit = False)

        account.save() 

        messages.add_message(req, constants.SUCCESS, 'Account created successfully!')

        return redirect("manage") 
            
    else:
        for error in details.errors:
            messages.add_message(req, constants.ERROR, f'Field "{error}": {details.errors[error][0]}')
        return redirect("manage") 

def create_category(req):
    if req.method != 'POST':
        return HttpResponse(status=405)
    

    details = CategoryForm(req.POST)

    if details.is_valid(): 
        category = details.save(commit = False)

        category.save() 

        messages.add_message(req, constants.SUCCESS, 'Category created successfully!')

        return redirect("manage") 
            
    else:
        for error in details.errors:
            messages.add_message(req, constants.ERROR, f'Field "{error}": {details.errors[error][0]}')
        return redirect("manage") 
    
def delete_account(req, id):
    account = Account.objects.get(id=id)

    account.delete()

    messages.add_message(req, constants.SUCCESS, 'Account deleted successfully!')

    return redirect("manage") 
