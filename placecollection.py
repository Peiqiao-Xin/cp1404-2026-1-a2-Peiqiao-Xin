import json
from operator import attrgetter

from place import Place


class PlaceCollection:
    """Manage a collection of Place objects."""

    def __init__(self):
        """Initialise an empty collection of places."""
        self.places = []

    def load_places(self, filename):
        """
        Load places from a JSON file into the places list.

        Expected JSON format:
        [
            {
                "name": "Lima",
                "country": "Peru",
                "priority": 3,
                "is_visited": false
            }
        ]
        """
        with open(filename, "r", encoding="utf-8") as in_file:
            data = json.load(in_file)
        self.places = [Place(item["name"], item["country"], item["priority"], item["is_visited"])
                       for item in data]

    def save_places(self, filename):
        """Save the places list to a JSON file."""
        with open(filename, "w", encoding="utf-8") as out_file:
            json.dump([place.__dict__ for place in self.places], out_file, indent=4)

    def add_place(self, place):
        """Add a single Place object to the collection."""
        self.places.append(place)

    def get_number_of_unvisited_places(self):
        """Return the number of places that have not been visited."""
        return sum(not place.is_visited for place in self.places)

    def sort(self, key):
        """Sort places by the given key, then by priority."""
        self.places.sort(key=attrgetter(key, "priority"))