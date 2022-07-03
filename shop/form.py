from attr import fields
from django  import forms
from .models import Order

class OrderForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    

    
    name = forms.CharField( widget=forms.TextInput(
        attrs={
            'placeholder': 'Your name',
            "class": "form-control",
        }
    ))
    
    email = forms.CharField( widget=forms.TextInput(
        attrs={
            'placeholder': 'Your email',
            "class": "form-control",
        }
    ))
    
    address = forms.CharField( widget=forms.TextInput(
        attrs={
            'placeholder': 'Your address',
            "class": "form-control",
        }
    ))
    
    city = forms.CharField( widget=forms.TextInput(
        attrs={
            'placeholder': 'Your city',
            "class": "form-control",
        }
    ))
    
    country = forms.CharField( widget=forms.TextInput(
        attrs={
            'placeholder': 'Your country',
            "class": "form-control",
        }
    ))
    
    zipcode = forms.CharField( widget=forms.TextInput(
        attrs={
            'placeholder': 'Your zipcode',
            "class": "form-control",
        }
    ))
    
    total = forms.CharField( widget=forms.TextInput(
        attrs={
            'readonly':'readonly',
            "class": "form-control",
            "id": "total",
        }
    ))
    
    
    
    class Meta:
        model = Order
        fields = ( '__all__'
                    # 'name',
                    # 'email',
                    # 'address' ,
                    # 'city' ,
                    # 'country' ,
                    # 'zipcode' 
                    )
        
        widgets={'items': forms.HiddenInput()}