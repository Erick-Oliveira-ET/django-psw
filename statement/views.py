from django.shortcuts import render
from user_profile.models import Category, Account

# Create your views here.
def create_value(req):
    if req.method == 'GET':
        categories= Category.objects.all()
        accounts= Account.objects.all()

        return render(req, 'create_value.html', {"categories": categories, "accounts":accounts})