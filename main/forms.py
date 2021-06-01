from django import forms

from model import models


class OrderForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = {
            'name',
            'email',
            'phonenumber',
            'description'
        }

    field_order = ['name', 'email', 'phonenumber', 'description']
