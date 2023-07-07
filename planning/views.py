from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from user_profile.models import Category

# Create your views here.
def view_planning(req):
    categories = Category.objects.all()

    return render(req, 'view_planning.html', {'categories': categories})

# Create your views here.
def define_planning(req):
    categories = Category.objects.all()

    return render(req, 'define_planning.html', {'categories': categories})

@csrf_exempt
def update_value_category(req, id):
    new_value = json.load(req)['new_value']
    category = Category.objects.get(id=id)
    category.planning_value = new_value
    category.save()

    return JsonResponse({'status': 'Success'})