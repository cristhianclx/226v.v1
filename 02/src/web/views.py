from django.shortcuts import render, redirect
from web.forms import SearchForm
from web.models import Search
from web.utils import normalize
from web.ml import predict

import pandas as pd


def homeView(request):
    if request.method == "GET":
        form = SearchForm()
        return render(request, "home.html", {"form": form,})
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            item = form.save()
            data = pd.DataFrame({
                "Fecha-I": item.date_to_search.strftime("%Y-%m-%d %H:%M:%S"),
                "MES": item.month_name,
                "OPERA": item.enterprise,
                "DIANOM": item.day_name,
            }, index=[0])
            features = normalize(data)
            results = predict(features)
            prediction = results[0]
            item.prediction = prediction
            item.save()
            return redirect("/results/{}".format(item.id))
        else:
            return render(request, "home.html", {"form": form,})


def resultsView(request, id):
    item = Search.objects.get(id = id)
    return render(request, "results.html", {"item": item})