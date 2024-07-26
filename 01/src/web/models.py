from django.db import models


class Person(models.Model):
    name = models.CharField(
        verbose_name="Name (name of a person)",
        max_length=100,
        blank=False,
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="Age (age of a person)",
        blank=False,
    )
    description = models.TextField(
        verbose_name="Description (description of a person)",
        blank=True,
    )
    created = models.DateTimeField(
        verbose_name="Created",
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name="Updated",
        auto_now=True,
    )

    def __str__(self):
        return self.name
    

class PersonDetail(models.Model):
    person = models.ForeignKey(
        Person,
        verbose_name="Person",
        blank=False,
        on_delete=models.CASCADE,
    )
    details = models.TextField(
        verbose_name="Details",
        blank=False,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="Rate (1-5)",
        blank=False,
    )
    created = models.DateTimeField(
        verbose_name="Created",
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name="Updated",
        auto_now=True,
    )

    def __str__(self):
        return f"{self.person.name} - {self.details}"
