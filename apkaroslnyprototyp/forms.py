from django.forms import ModelForm, Form
from django.forms import widgets
from apkaroslnyprototyp.models import *
from django import forms

class TradeForm(ModelForm):
    class Meta:
        model = TradePost
        exclude = ['id', 'add_date', 'reacted']

class GuideForm(ModelForm):
    class Meta:
        model = Guide
        fields = ['title', 'content']

class ProfieForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location']
        widgets = {'bio':forms.Textarea()}
