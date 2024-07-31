from django import forms
from web.models import Search


class SearchForm(forms.ModelForm):
    cv = forms.FileField(
        label="Upload CV",
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "accept": ".docx",
            }
        )
    )

    class Meta:
        model = Search
        fields = ("cv",)