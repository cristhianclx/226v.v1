from django.core.validators import FileExtensionValidator
from django.db import models


class Search(models.Model):
    cv = models.FileField(
        upload_to="cv",
        blank=False,
        validators=[FileExtensionValidator(allowed_extensions=["docx"])]
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Search(models.Model):
    cv = models.FileField(
        upload_to="cv",
        blank=False,
        validators=[FileExtensionValidator(allowed_extensions=["docx", "pdf"])]
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Match(models.Model):
    search = models.ForeignKey(
        Search,
        on_delete=models.CASCADE,
    )
    position = models.CharField(
        max_length=255,
        blank=False
    )
    url = models.URLField(
        blank=True,
    )
    ranking = models.DecimalField(
        max_digits=30,
        decimal_places=25
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
