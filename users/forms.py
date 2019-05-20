from .models import User
from django import forms
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'validate',
                                            'placeholder': ''
                                        }),
            'password': forms.PasswordInput(attrs={'class': 'validate',
                                                   'placeholder': ''
                                                })
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'sex', 'ocupatie', 'varsta', 'telefon', 'imagine') 
    

