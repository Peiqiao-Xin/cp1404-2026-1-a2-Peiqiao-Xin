"""
Tests for PlaceCollection class.
"""

from place import Place
from placecollection import PlaceCollection


def main():
    """Run simple tests for PlaceCollection class."""
    test_add_place()
    test_get_number_of_unvisited_places()
    test_sort()
    test_load_and_save_places()


def test_add_place():
    """Test adding a place to the collection."""
    place_collection = PlaceCollection()
    place = Place("Lima", "Peru", 3, False)
    place_collection.add_place(place)

    print("number of places:", len(place_collection.places), "(expected: 1)")
    print("first place:", place_collection.places[0], "(expected: Lima in Peru (priority 3) - unvisited)")


def test_get_number_of_unvisited_places():
    """Test counting unvisited places."""
    place_collection = PlaceCollection()
    place_collection.add_place(Place("Lima", "Peru", 3, False))
    place_collection.add_place(Place("Rome", "Italy", 1, True))
    place_collection.add_place(Place("Tokyo", "Japan", 2, False))

    print("unvisited count:", place_collection.get_number_of_unvisited_places(), "(expected: 2)")


def test_sort():
    """Test sorting places by a given key, then by priority."""
    place_collection = PlaceCollection()
    place_collection.add_place(Place("Lima", "Peru", 3, False))
    place_collection.add_place(Place("Rome", "Italy", 1, True))
    place_collection.add_place(Place("Tokyo", "Japan", 2, False))
    place_collection.add_place(Place("Auckland", "New Zealand", 1, True))

    place_collection.sort("country")
    print("sorted by country:")
    for place in place_collection.places:
        print(place)
    print("expected first place: Rome in Italy (priority 1) - visited")
    print("expected second place: Tokyo in Japan (priority 2) - unvisited")
    print("expected third place: Auckland in New Zealand (priority 1) - visited")
    print("expected fourth place: Lima in Peru (priority 3) - unvisited")


def test_load_and_save_places():
    """Test loading and saving places using JSON."""
    place_collection = PlaceCollection()
    test_filename = "test_places.json"

    place_collection.add_place(Place("Lima", "Peru", 3, False))
    place_collection.add_place(Place("Rome", "Italy", 1, True))
    place_collection.save_places(test_filename)

    loaded_collection = PlaceCollection()
    loaded_collection.load_places(test_filename)

    print("loaded places:", len(loaded_collection.places), "(expected: 2)")
    print("first loaded place:", loaded_collection.places[0], "(expected: Lima in Peru (priority 3) - unvisited)")
    print("second loaded place:", loaded_collection.places[1], "(expected: Rome in Italy (priority 1) - visited)")


if __name__ == "__main__":
    main()