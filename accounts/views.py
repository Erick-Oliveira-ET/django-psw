from django.shortcuts import render

# Create your views here.
from user_profile.models import Category

# Create your views here.
def define_account(req):
    categories = Category.objects.all()

    return render(req, 'define_account.html', {'categories': categories})
