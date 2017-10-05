from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude=['created_by', 'updated_at', 'users']
