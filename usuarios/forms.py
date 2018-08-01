from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Character, World, Vocation, Guild
from .choices import *

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Nome do Char'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Senha'})
        }

    def save(self, commit=True):
        user = super(UserModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class CharacterModelForm(forms.ModelForm):
    vocation = forms.ModelChoiceField(queryset=Vocation.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Vocação'}))
    world = forms.ModelChoiceField(queryset=World.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Mundo'}))
    guild = forms.ModelChoiceField(queryset=Guild.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Guild'}))

    class Meta:
        model = Character
        fields = [
            'name',
            'level',
            'vocation',
            'world'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Nome do Char'}),
            'level': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Level'})
        }

