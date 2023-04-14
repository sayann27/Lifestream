from django import forms
from home.models import Hospital

class Hospital(forms.ModelForm):
    class Meta:
        model = "Hospital"
        fields = "__all__"