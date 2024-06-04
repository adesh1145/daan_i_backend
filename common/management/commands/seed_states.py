from django.core.management.base import BaseCommand
from common.models.state_city_models import *


class Command(BaseCommand):
    help = "Seed the database with a list of states"

    def handle(self, *args, **kwargs):
        states = [
            "Andaman & Nicobar Islands",
            "Andhra Pradesh",
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Chandigarh",
            "Chhattisgarh",
            "Dadra & Nagar Haveli & Daman & Diu",
            "Delhi",
            "Goa",
            "Gujarat",
            "Haryana",
            "Himachal Pradesh",
            "Jammu & Kashmir",
            "Jharkhand",
            "Karnataka",
            "Kerala",
            "Madhya Pradesh",
            "Maharashtra",
            "Manipur",
            "Meghalaya",
            "Mizoram",
            "Nagaland",
            "Odisha",
            "Panducherry",
            "Punjab",
            "Rajasthan",
            "Sikkim",
            "Tamil Nadu",
            "Telangana",
            "Tripura",
            "Uttarakhand",
            "Uttar Pradesh",
            "West Bengal",
        ]

        for state_name in states:
            state, created = StateModel.objects.get_or_create(name=state_name)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added state: {state_name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"State already exists: {state_name}")
                )
