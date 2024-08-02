from django.shortcuts import render, redirect
from django.views.generic import View
from web.forms import SearchForm
from web.models import Search, Match
from web.utils import getText, wrangler

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle


job_matrix = pickle.load(open("./src/web/data/job_matrix.pickle", "rb"))
job_vectorizer = pickle.load(open("./src/web/data/job_vectorizer.pickle", "rb"))
ranker = pd.read_pickle("./src/web/data/puestos.pickle")


class HomeView(View):
    def get(self, request):
        form = SearchForm()
        return render(request, "home.html", {"form": form})

    def post(self, request):
        form = SearchForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            cv_in_text = getText(instance.cv)
            cv_clean_in_text = wrangler(cv_in_text)
            cv_serie = pd.Series(cv_clean_in_text)
            cv_matrix = job_vectorizer.transform(cv_serie)
            ranking = cosine_similarity(cv_matrix, job_matrix, True)
            ranking_serie = pd.Series(ranking[0])
            ranker["RANKING"] = ranking_serie
            ranker_final = ranker.sort_values("RANKING", ascending=False)
            for r in ranker_final.index:
                if ranker_final["RANKING"][r] >= 0.3:
                    Match.objects.create(
                        search=instance,
                        position=ranker_final["PUESTO"][r],
                        url=ranker_final["URL"][r],
                        ranking=ranker_final["RANKING"][r] * 100,
                    )
            return redirect("results", id=instance.id)
        else:
            return redirect("home")


class ResultsView(View):
    def get(self, request, id):
        instance = Search.objects.get(id=id)
        matches = Match.objects.filter(search=instance).all().order_by("-ranking")
        return render(request, "results.html", {"matches": matches})
