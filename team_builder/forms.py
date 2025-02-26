from django import forms
from .models import Team, Strategy

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'units', 'size_limit']

class StrategyForm(forms.ModelForm):
    class Meta:
        model = Strategy
        fields = ['title', 'description']
