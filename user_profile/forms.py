from django.forms import ModelForm
from .models import Account, Category

# define the class of a form
class AccountForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Account
        fields = [ "nickname","bank" ,"bank_type" ,"value","icon"]

class CategoryForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Category	
        fields = ["category","essential"]