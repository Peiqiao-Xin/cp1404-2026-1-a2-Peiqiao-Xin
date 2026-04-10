"""
Tests for Place class.
"""

from place import Place


def main():
    """Run simple tests for Place class."""
    test_place_init()
    test_place_str()
    test_mark_visited()
    test_mark_unvisited()
    test_is_important()


def test_place_init():
    """Test Place initialisation."""
    place = Place("Lima", "Peru", 3, False)
    print("name:", place.name, "(expected: Lima)")
    print("country:", place.country, "(expected: Peru)")
    print("priority:", place.priority, "(expected: 3)")
    print("is_visited:", place.is_visited, "(expected: False)")


def test_place_str():
    """Test string representation of Place."""
    place = Place("Lima", "Peru", 3, False)
    print("str(place):", str(place), "(expected: Lima in Peru (priority 3) - unvisited)")
    visited_place = Place("Rome", "Italy", 1, True)
    print("str(visited_place):", str(visited_place), "(expected: Rome in Italy (priority 1) - visited)")


def test_mark_visited():
    """Test marking a place as visited."""
    place = Place("Lima", "Peru", 3, False)
    place.mark_visited()
    print("is_visited after mark_visited:", place.is_visited, "(expected: True)")


def test_mark_unvisited():
    """Test marking a place as unvisited."""
    place = Place("Rome", "Italy", 1, True)
    place.mark_unvisited()
    print("is_visited after mark_unvisited:", place.is_visited, "(expected: False)")


def test_is_important():
    """Test important place logic."""
    important_place = Place("Rome", "Italy", 1, False)
    also_important_place = Place("Tokyo", "Japan", 2, True)
    not_important_place = Place("Lima", "Peru", 3, False)

    print("important_place.is_important():", important_place.is_important(), "(expected: True)")
    print("also_important_place.is_important():", also_important_place.is_important(), "(expected: True)")
    print("not_important_place.is_important():", not_important_place.is_important(), "(expected: False)")


if __name__ == "__main__":
    main()