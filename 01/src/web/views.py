from django.shortcuts import render

from web.models import Person


# CUD
# create
# update
# delete


def personsView(request):
    items = Person.objects.all()
    return render(request, "persons-list.html", {
        "items": items,
    })


def personsDetailView(request, id):
    item = Person.objects.get(id = id)
    return render(request, "persons-detail.html", {
        "item": item,
    })