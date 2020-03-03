from apkaroslnyprototyp.models import *
from django import forms

class TradeForm(forms.Form):
    class Meta:
        model = TradePost
        exclude = ['id', 'add_date']