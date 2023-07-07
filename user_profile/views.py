from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

from .forms import CategoryForm, AccountForm
from .models import Account, Category
from .utils import get_total

# Create your views here.
def home(req):
    accounts = Account.objects.all()
    account_total_value = get_total(Account, "value")

    return render(req, "home.html",  {"accounts": accounts, "account_total_value": account_total_value})

def manage(req):
    accounts = Account.objects.all()
    account_total_value = get_total(Account, "value")

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

def toggle_category_essential(req, id):
    category = Category.objects.get(id=id)

    category.essential = not category.essential 
    
    category.save()

    return redirect("manage") 
