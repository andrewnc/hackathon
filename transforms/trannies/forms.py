from django import forms

class NameForm(forms.Form):
    text_input = forms.CharField(label='Your name', max_length=100)