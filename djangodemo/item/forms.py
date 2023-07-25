from django.forms import ModelForm, forms
from django.forms.widgets import Select, TextInput, Textarea, FileInput

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(ModelForm):
    class Meta: 
        model = Item 
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': Select(attrs={
                'class': INPUT_CLASSES
            }), 
            'name': TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': INPUT_CLASSES
            }), 
            'price': TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(ModelForm):
    class Meta: 
        model = Item 
        fields = ('name', 'description', 'price', 'image', )
        widgets = {
            'name': TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': INPUT_CLASSES
            }), 
            'price': TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


