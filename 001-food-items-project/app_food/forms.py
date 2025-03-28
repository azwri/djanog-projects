from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter item name', 'class': 'input'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter item description', 'class': 'input'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter item price', 'class': 'input', type: 'number'}),
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'file-input'}),
        }
        labels = {
            'name': 'Item Name',
            'description': 'Item Description',
            'price': 'Item Price',
            'image': 'Item Image',
        }
        help_texts = {
            'name': 'Name of the item',
            'description': 'Description of the item',
            'price': 'Price of the item in USD',
            'image': 'Upload an image of the item',
        }
        error_messages = {
            'name': {
                'required': 'This field is required.',
                'max_length': 'This field cannot exceed 100 characters.',
            },
            'description': {
                'required': 'This field is required.',
            },
            'price': {
                'required': 'This field is required.',
                'invalid': 'Enter a valid price.',
            },
            'image': {
                'invalid': 'Upload a valid image file.',
            },
        }