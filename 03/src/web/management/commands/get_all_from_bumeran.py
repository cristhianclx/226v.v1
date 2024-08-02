from django.core.management.base import BaseCommand
from datetime import datetime
from django.utils.text import slugify
from web.utils import wrangler
import pandas as pd
import requests
import csv
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


class Command(BaseCommand):
    help = "This is a command to get all from bumeran"

    def obtainData(self):
        data = []
        url = "https://www.bumeran.com.pe/api/avisos/searchV2?pageSize=100&page=0&sort=RELEVANTES"
        raw_from_bumeran = requests.post(
            url,
            headers={
                "Host": "www.bumeran.com.pe",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0",
                "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.8,es-ES;q=0.5,es;q=0.3",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Content-Type": "application/json",
                "x-site-id": "BMPE",
                "Origin": "https://www.bumeran.com.pe",
                "DNT": "1",
                "Connection": "keep-alive",
                "Referer": "https://www.bumeran.com.pe/empleos.html",
            },
            data='{"filtros":[]}',
        )
        raw_from_bumeran = raw_from_bumeran.json()
        for x in raw_from_bumeran["content"]:
            data.append(
                {
                    "FECHA_SCRAP": "{}".format(
                        datetime.now().strftime("%d/%m/%Y %H:%M")
                    ),
                    "CATEGORIA": "",
                    "FUNCION": "",
                    "EMPRESA": x["empresa"],
                    "PUESTO": x["titulo"],
                    "DESCRIPCION": x["detalle"],
                    "URL": "https://www.bumeran.com.pe/empleos/{}-{}-{}.html".format(
                        slugify(x["titulo"]), slugify(x["empresa"]), x["id"]
                    ),
                }
            )
        return data

    def handle(self, *args, **options):
        file_id = "{}".format(datetime.now().strftime("%Y%m%d-%H%M"))
        csv_filename = "./src/web/data/{}.csv".format(file_id)
        raw = self.obtainData()
        with open(csv_filename, "w") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=[
                    "FECHA_SCRAP",
                    "CATEGORIA",
                    "FUNCION",
                    "EMPRESA",
                    "PUESTO",
                    "DESCRIPCION",
                    "URL",
                ],
            )
            writer.writeheader()
            for row in raw:
                writer.writerow(row)
        job_raw = pd.read_csv(csv_filename)
        job_raw["DESC_PUESTO"] = job_raw["PUESTO"] + " " + job_raw["DESCRIPCION"]
        job_raw["DESC_LIMPIO"] = job_raw.apply(
            lambda row: wrangler(row["DESC_PUESTO"]), axis=1
        )
        job_vectorizer = TfidfVectorizer()
        job_matrix = job_vectorizer.fit_transform(job_raw["DESC_LIMPIO"])
        pickle.dump(job_vectorizer, open("./src/web/data/job_vectorizer.pickle", "wb"))
        pickle.dump(job_matrix, open("./src/web/data/job_matrix.pickle", "wb"))
        job_puesto = job_raw[["PUESTO", "URL"]]
        job_puesto.to_pickle("./src/web/data/puestos.pickle")
