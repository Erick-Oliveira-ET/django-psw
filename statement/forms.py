from django.forms import ModelForm
from .models import Values

# define the class of a form
class ValueForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Values
        fields = [ 
            'value',
            'category',
            'description',
            'date',
            'account',
            'type',

        ]
