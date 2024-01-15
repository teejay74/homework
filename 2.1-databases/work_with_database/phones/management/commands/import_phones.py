import csv
from pathlib import Path

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        csv_file_path = 'phones.csv'

        csv_path = Path(csv_file_path)

        if not csv_path.is_file():
            self.stdout.write(self.style.ERROR(f'Файл {csv_file_path} не существует.'))
            return

        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            item = Phone(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists']
            )
            item.save()

            self.stdout.write(self.style.SUCCESS('Данные успешно импортированы.'))
