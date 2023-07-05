from django.db.models import Sum

def get_total(model, field):
    return model.objects.all().aggregate(Sum(field))[f'{field}__sum']