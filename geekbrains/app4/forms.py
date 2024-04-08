from django import forms
from datetime import datetime


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18, max_value=120)


class TestFields(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18, max_value=120)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=True, initial=True)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    # Виджеты
    v_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Плейсхолдер'}))
    v_birthdate = forms.DateField(
        initial=datetime.now().date(),
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        )
    )
    # forms.Textarea()
    # forms.PasswordInput()
    # forms.NumberInput()
    # forms.CheckboxInput()
    # forms.DateInput()
    # forms.FileInput()

    def clean_email(self):
        if not (self.cleaned_data['email'].endswith('.ru')):
            raise forms.ValidationError('Принимается электронная почта только в домене .ru')
        return self.cleaned_data['email']
