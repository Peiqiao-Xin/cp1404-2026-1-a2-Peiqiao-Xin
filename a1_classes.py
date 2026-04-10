"""
CP1404/CP5632 Assignment 2 - Travel Tracker 2.0

Name: Peiqiao Xin
Date: 08/04/2026
GitHub repository: https://github.com/Peiqiao-Xin/cp1404-2026-1-a2-Peiqiao-Xin.git

Console version of Travel Tracker using Place and PlaceCollection classes.
"""

import random

from place import Place
from placecollection import PlaceCollection

FILENAME = "places.json"


def main():
    """Run the Travel Tracker console program using classes."""
    print("Travel Tracker 1.0 - by Peiqiao Xin")
    place_collection = PlaceCollection()

    try:
        place_collection.load_places(FILENAME)
        print(f"{len(place_collection.places)} places loaded from {FILENAME}")
    except FileNotFoundError:
        print(f"File {FILENAME} not found")
        return

    menu_choice = ""
    while menu_choice != "Q":
        print_menu()
        menu_choice = input(">>> ").strip().upper()

        if menu_choice == "D":
            display_places(place_collection)
        elif menu_choice == "R":
            recommend_place(place_collection)
        elif menu_choice == "A":
            add_place(place_collection)
        elif menu_choice == "M":
            mark_place_visited(place_collection)
        elif menu_choice == "Q":
            place_collection.save_places(FILENAME)
            print(f"{len(place_collection.places)} places saved to {FILENAME}")
            print("Have a nice day :)")
        else:
            print("Invalid menu choice")


def print_menu():
    """Display the program menu."""
    print("Menu:")
    print("D - Display all places")
    print("R - Recommend a random place")
    print("A - Add a new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def display_places(place_collection):
    """Display all places sorted by visited status then priority."""
    place_collection.sort("is_visited")

    max_name_width = max(len(place.name) for place in place_collection.places)
    max_country_width = max(len(place.country) for place in place_collection.places)

    for index, place in enumerate(place_collection.places, start=1):
        marker = "*" if not place.is_visited else ""
        print(
            f"{marker}{index}. "
            f"{place.name:<{max_name_width}} in "
            f"{place.country:<{max_country_width}} "
            f"{place.priority}"
        )

    unvisited_count = place_collection.get_number_of_unvisited_places()
    print(f"{len(place_collection.places)} places tracked. "
          f"You still want to visit {unvisited_count} places.")


def recommend_place(place_collection):
    """Recommend a random unvisited place."""
    unvisited_places = [place for place in place_collection.places if not place.is_visited]

    if not unvisited_places:
        print("No places left to visit!")
    else:
        random_place = random.choice(unvisited_places)
        print("Not sure where to visit next?")
        print(f"How about... {random_place.name} in {random_place.country}?")


def add_place(place_collection):
    """Prompt for a new place and add it to the collection."""
    name = get_non_blank_string("Name: ")
    country = get_non_blank_string("Country: ")
    priority = get_positive_number("Priority: ")

    new_place = Place(name, country, priority, False)
    place_collection.add_place(new_place)
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def mark_place_visited(place_collection):
    """Mark a selected place as visited if possible."""
    if place_collection.get_number_of_unvisited_places() == 0:
        print("No unvisited places")
        return

    display_places(place_collection)
    print("Enter the number of a place to mark as visited")

    place_number = get_valid_place_number(place_collection)
    selected_place = place_collection.places[place_number - 1]

    if selected_place.is_visited:
        print(f"You have already visited {selected_place.name}")
    else:
        selected_place.mark_visited()
        print(f"{selected_place.name} in {selected_place.country} visited!")


def get_non_blank_string(prompt):
    """Prompt for a non-blank string and return it."""
    user_input = input(prompt).strip()
    while user_input == "":
        print("Input can not be blank")
        user_input = input(prompt).strip()
    return user_input


def get_positive_number(prompt):
    """Prompt for a positive integer greater than 0 and return it."""
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number must be > 0")
            else:
                return number
        except ValueError:
            print("Invalid input; enter a valid number")


def get_valid_place_number(place_collection):
    """Prompt for a valid place number and return it."""
    while True:
        try:
            place_number = int(input(">>> "))
            if place_number <= 0:
                print("Number must be > 0")
            else:
                try:
                    place_collection.places[place_number - 1]
                    return place_number
                except IndexError:
                    print("Invalid place number")
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == "__main__":
    main()