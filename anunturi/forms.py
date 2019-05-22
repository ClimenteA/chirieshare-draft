from .models import Anunturi, Mesaje
from django import forms
from django.forms import ModelForm


class AnunturiForm(ModelForm):

    class Meta:
        model = Anunturi
        fields = "__all__"
        
        comm_attrs = {'class': 'validate','placeholder': ''}

        widgets = {
            'tip_inchiriere': forms.RadioSelect(attrs={'class': 'with-gap',
                                                   'placeholder': ''
                                                }),
            'localitate': forms.TextInput(attrs=comm_attrs),
            'zona': forms.TextInput(attrs=comm_attrs),
            'pret': forms.NumberInput(attrs=comm_attrs),
            'facilitati': forms.SelectMultiple(),
            'user': forms.Select(),
            'descriere_anunt': forms.Textarea(attrs={"class": "materialize-textarea", 'placeholder': ''}),
        }

    
class MesajeForm(ModelForm):

     class Meta:
        model = Mesaje
        fields = "__all__"

        widgets = {'mesaj_primit': forms.Textarea(attrs={"class": "materialize-textarea", 'placeholder': ''}),
                   'mesaj_trimis': forms.Textarea(attrs={"class": "materialize-textarea", 'placeholder': ''}),
        }

