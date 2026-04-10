"""
CP1404/CP5632 Assignment 2 - Travel Tracker 2.0

Name: Peiqiao Xin
Date: 08/04/2026
GitHub repository: https://github.com/Peiqiao-Xin/cp1404-2026-1-a2-Peiqiao-Xin.git

Kivy GUI program for Travel Tracker using Place and PlaceCollection classes.
"""

from operator import attrgetter

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from place import Place
from placecollection import PlaceCollection

FILENAME = "places.json"
VISITED_COLOUR = (0.25, 0.25, 0.25, 1)
UNVISITED_COLOUR = (0.0, 0.45, 0.45, 1)

SORT_OPTIONS = {
    "Name": "name",
    "Country": "country",
    "Priority": "priority",
    "Visited": "is_visited"
}


class TravelTrackerApp(App):
    """Main Kivy app for Travel Tracker."""

    def __init__(self, **kwargs):
        """Initialise app and data model."""
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()

    def build(self):
        """Build the GUI and load data."""
        self.title = "Travel Tracker 2.0"
        self.root = Builder.load_file("app.kv")
        self.load_places()
        self.place_collection.places.sort(key=attrgetter("name", "priority"))
        self.create_place_buttons()
        self.update_top_status_label()
        self.set_bottom_status("Welcome to Travel Tracker 2.0")
        return self.root

    def load_places(self):
        """Load places from the JSON file."""
        self.place_collection.load_places(FILENAME)

    def on_stop(self):
        """Save places when the program closes."""
        self.place_collection.save_places(FILENAME)

    def create_place_buttons(self):
        """Create buttons for all places."""
        self.root.ids.places_box.clear_widgets()
        for place in self.place_collection.places:
            button = Button(
                text=str(place),
                size_hint_y=None,
                height="60dp",
                background_normal=""
            )
            button.place = place
            self.update_button_colour(button, place)
            button.bind(on_release=self.press_place_button)
            self.root.ids.places_box.add_widget(button)

    def update_button_colour(self, button, place):
        """Set button colour based on visited status."""
        if place.is_visited:
            button.background_color = VISITED_COLOUR
        else:
            button.background_color = UNVISITED_COLOUR

    def press_place_button(self, instance):
        """Handle clicking a place button."""
        place = instance.place

        if place.is_visited:
            place.mark_unvisited()
            if place.is_important():
                message = f"You need to visit {place.name}. Get going!"
            else:
                message = f"You need to visit {place.name}."
        else:
            place.mark_visited()
            if place.is_important():
                message = f"You visited {place.name}. Great travelling!"
            else:
                message = f"You visited {place.name}."

        instance.text = str(place)
        self.update_button_colour(instance, place)
        self.update_top_status_label()
        self.set_bottom_status(message)

    def add_place(self):
        """Add a new place after validating input."""
        name = self.root.ids.name_input.text.strip()
        country = self.root.ids.country_input.text.strip()
        priority_text = self.root.ids.priority_input.text.strip()

        if not name or not country or not priority_text:
            self.set_bottom_status("All fields must be completed")
            return

        try:
            priority = int(priority_text)
        except ValueError:
            self.set_bottom_status("Please enter a valid number")
            return

        if priority <= 0:
            self.set_bottom_status("Priority must be > 0")
            return

        new_place = Place(name, country, priority, False)
        self.place_collection.add_place(new_place)
        current_sort = self.root.ids.sort_spinner.text
        if current_sort in SORT_OPTIONS:
            self.sort_places(current_sort)
        else:
            self.place_collection.places.sort(key=attrgetter("name", "priority"))
            self.create_place_buttons()

        self.clear_entry_fields()
        self.set_bottom_status(f"{new_place.name} in {new_place.country} (priority {new_place.priority}) added")
        self.update_top_status_label()

    def clear_fields(self):
        """Clear all entry fields and the status message."""
        self.clear_entry_fields()
        self.set_bottom_status("")

    def clear_entry_fields(self):
        """Clear text input fields and reset focus."""
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""
        self.root.ids.name_input.focus = True

    def sort_places(self, sort_text):
        """Sort places and refresh buttons."""
        key = SORT_OPTIONS.get(sort_text)
        if key:
            self.place_collection.places.sort(key=attrgetter(key, "priority"))
            self.create_place_buttons()

    def update_top_status_label(self):
        """Update the top status label with unvisited count."""
        unvisited_count = self.place_collection.get_number_of_unvisited_places()
        self.root.ids.top_status_label.text = f"Places to visit: {unvisited_count}"

    def set_bottom_status(self, message):
        """Set the bottom status message."""
        self.root.ids.bottom_status_label.text = message


if __name__ == "__main__":
    TravelTrackerApp().run()