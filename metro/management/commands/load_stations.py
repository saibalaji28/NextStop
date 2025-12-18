import json
from pathlib import Path
from django.core.management.base import BaseCommand
from metro.models import Station, Connection

class Command(BaseCommand):
    help = "Load Delhi Metro stations and connections from JSON file"

    def handle(self, *args, **kwargs):
        path = Path("metro/data/stations.json")

        with open(path, "r") as file:
            data = json.load(file)

        station_map = {}

        # Create stations
        for name in data["stations"]:
            station, _ = Station.objects.get_or_create(name=name)
            station_map[name] = station

        # Create connections (both directions)
        for conn in data["connections"]:
            from_station = station_map[conn["from"]]
            to_station = station_map[conn["to"]]
            distance = conn["distance"]

            Connection.objects.get_or_create(
                from_station=from_station,
                to_station=to_station,
                distance=distance
            )

            Connection.objects.get_or_create(
                from_station=to_station,
                to_station=from_station,
                distance=distance
            )

        self.stdout.write(self.style.SUCCESS("Metro data loaded successfully"))