import csv

from django.conf import settings


def load_csv():
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)