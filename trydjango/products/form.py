from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price',
        ]

class RawProductForm(forms.Form):
    title = forms.CharField() 
    description = forms.CharField(
        required=False,
        label = "pias",
        widget=forms.EmailInput(
            
                attrs={
                    "placeholder": "your description",
                }
                    )
                )
    price = forms.DecimalField()
