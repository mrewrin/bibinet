from django.core.management.base import BaseCommand
from bibinet.bibinet.main.models import Mark, Model


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        marks = [
            {"name": "Honda", "producer_country_name": "Japan"},
            {"name": "Toyota", "producer_country_name": "Japan"},
            {"name": "Ford", "producer_country_name": "USA"},
            {"name": "BMW", "producer_country_name": "Germany"},
            {"name": "Audi", "producer_country_name": "Germany"}
        ]
        for mark in marks:
            Mark.objects.create(**mark)

        models = [
            {"name": "Civic", "mark_id": 1},
            {"name": "Accord", "mark_id": 1},
            {"name": "Corolla", "mark_id": 2},
            {"name": "Mustang", "mark_id": 3},
            {"name": "X5", "mark_id": 4}
        ]
        for model in models:
            Model.objects.create(**model)