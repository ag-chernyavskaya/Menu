from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    class Meta:
        model = Contact
        fields = ('name', 'email')
        widgets = {
            'name': forms.TextInput(attrs={"class": "editContent", "placeholder": "Your Name..."}),
            'email': forms.TextInput(attrs={"class": "editContent", "placeholder": "Your Email..."})
        }
        labels = {
            "name": '',
            "email": ''
        }