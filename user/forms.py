from django import forms

class RegisterForm(forms.Form):
    username = forms.Charfield()
    first_name = forms.Charfield()
    last_name = forms.Charfield()
    email= forms.EmailField()
    password = forms.Charfield()
