from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from web.forms import PersonForm
from web.models import Person


def personsView(request):
    items = Person.objects.all()
    return render(request, "persons/list.html", {
        "items": items,
    })


def personsDetailView(request, id):
    item = Person.objects.get(id = id)
    return render(request, "persons/detail.html", {
        "item": item,
    })


def personsAddView(request):
    if request.method == "GET":
        form = PersonForm()
        return render(request, "persons/add.html", {
            "form": form,
        })
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('persons-list'))
        else:
            return render(request, "persons/add.html", {
                "form": form,
            })
        

def personsUpdateView(request, id):
    item = Person.objects.get(id = id)
    if request.method == "GET":
        form = PersonForm(instance = item)
        return render(request, "persons/update.html", {
            "item": item,
            "form": form,
        })
    if request.method == "POST":
        form = PersonForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('persons-list'))
        else:
            return render(request, "persons/update.html", {
                "item": item,
                "form": form,
            })
        

def personsDeleteView(request, id):
    item = Person.objects.get(id = id)
    if request.method == "GET":
        return render(request, "persons/delete.html", {
            "item": item,
        })
    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect(reverse_lazy('persons-list'))