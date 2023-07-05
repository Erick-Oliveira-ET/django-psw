from django.shortcuts import render
from django.http import HttpResponse
from .forms import CategoryForm, AccountForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def home(req):
    return render(req, "home.html")

def manage(req):
    return render(req, "manage.html")

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
    
    details = CategoryForm(req.POST, req.FILES)

    if details.is_valid(): 
        category = details.save(commit = False)

        category.save() 

        return redirect("manage") 
            
    else:
        return redirect("manage") 
