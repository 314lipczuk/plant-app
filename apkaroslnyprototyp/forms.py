from django.forms import ModelForm

from apkaroslnyprototyp.models import *
from django import forms

class TradeForm(ModelForm):
    class Meta:
        model = TradePost
        exclude = ['id', 'add_date']