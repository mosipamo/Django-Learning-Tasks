from .models import Link
from django import forms as f

class LinkForm(f.ModelForm):
    class Meta:
        model = Link
        fields = ["name", "url", "slug"]