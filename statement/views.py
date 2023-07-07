from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime

from user_profile.models import Category, Account
from .forms import ValueForm
from .models import Values

def view_statement(request):
    account = Account.objects.all()
    category = Category.objects.all()

    account_get = request.GET.get('account')
    category_get = request.GET.get('category')
    values = Values.objects.filter(date__month=datetime.now().month)

    if account_get:
        values = values.filter(account__id=account_get)
    if category_get:
        values = values.filter(category__id=category_get)
 

    return render(request, 'view_statement.html', {'values': values, 'accounts': account, 'categories': category})
    

# Create your views here.
def create_value(req):
    if req.method == 'GET':
        categories= Category.objects.all()
        accounts= Account.objects.all()

        return render(req, 'create_value.html', {"categories": categories, "accounts":accounts})
    elif req.method == 'POST':
        details = ValueForm(req.POST)

        if details.is_valid(): 
            value = details.save(commit = False)

            value.save() 

            messages.add_message(req, constants.SUCCESS, 'Statement created successfully!')

            account = Account.objects.get(id=value.account_id)

            if value.type == "I":
                account.value += value.value
            else:
                account.value -= value.value
 
            account.save()

            return redirect("create_value") 
        else:
            for error in details.errors:
                messages.add_message(req, constants.ERROR, f'Field "{error}": {details.errors[error][0]}')
            return redirect("create_value") 
