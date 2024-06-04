from django.core.management.base import BaseCommand
from common.models.state_city_models import StateModel, CityModel


class Command(BaseCommand):
    help = "Seed the database with a list of cities"

    def handle(self, *args, **kwargs):
        cities = {
            "Uttar Pradesh": [
                "Agra",
                "Aligarh",
                "Prayagraj",
                "Ambedkar Nagar",
                "Amethi",
                "Amroha",
                "Auraiya",
                "Azamgarh",
                "Baghpat",
                "Bahraich",
                "Ballia",
                "Balrampur",
                "Banda",
                "Barabanki",
                "Bareilly",
                "Basti",
                "Bhadohi",
                "Bijnor",
                "Budaun",
                "Bulandshahr",
                "Chandauli",
                "Chitrakoot",
                "Deoria",
                "Etah",
                "Etawah",
                "Ayodhya",
                "Farrukhabad",
                "Fatehpur",
                "Firozabad",
                "Gautam Buddha Nagar",
                "Ghaziabad",
                "Ghazipur",
                "Gonda",
                "Gorakhpur",
                "Hamirpur",
                "Hapur",
                "Hardoi",
                "Hathras",
                "Jalaun",
                "Jaunpur",
                "Jhansi",
                "Kannauj",
                "Kanpur Dehat",
                "Kanpur Nagar",
                "Kasganj",
                "Kaushambi",
                "Kheri",
                "Kushinagar",
                "Lalitpur",
                "Lucknow",
                "Maharajganj",
                "Mahoba",
                "Mainpuri",
                "Mathura",
                "Mau",
                "Meerut",
                "Mirzapur",
                "Moradabad",
                "Muzaffarnagar",
                "Pilibhit",
                "Pratapgarh",
                "Raebareli",
                "Rampur",
                "Saharanpur",
                "Sambhal",
                "Sant Kabir Nagar",
                "Shahjahanpur",
                "Shamli",
                "Shravasti",
                "Siddharthnagar",
                "Sitapur",
                "Sonbhadra",
                "Sultanpur",
                "Unnao",
                "Varanasi",
            ],
            # Add your states and cities here
        }

        for state_name, city_names in cities.items():
            state, created = StateModel.objects.get_or_create(name=state_name)
            for city_name in city_names:
                city, created = CityModel.objects.get_or_create(
                    name=city_name, state=state
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully added city: {city_name} in state: {state_name}"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f"City already exists: {city_name} in state: {state_name}"
                        )
                    )
