from django import forms
from web.models import Search


class SearchForm(forms.ModelForm):
    cv = forms.FileField(
        label="Upload CV",
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "accept": ".docx,.pdf",
            }
        )
    )

    class Meta:
        model = Search
        fields = ("cv",)