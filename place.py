"""
CP1404/CP5632 Assignment 2 - Travel Tracker
Place class

Represents a place with name, country, priority and visited status.
"""


class Place:
    """A class to represent a travel destination."""

    def __init__(self, name: str, country: str, priority: int, is_visited: bool):
        """
        Create a new Place object.

        :param name: Name of the place
        :param country: Country where the place is located
        :param priority: Priority level
        :param is_visited: True if the place has been visited, otherwise False
        """
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self) -> str:
        """Return a user-friendly string describing the place."""
        if self.is_visited:
            return f"{self.name} in {self.country}, priority {self.priority} (visited)"
        return f"{self.name} in {self.country}, priority {self.priority}"

    def mark_visited(self):
        """Set this place as visited."""
        self.is_visited = True

    def mark_unvisited(self):
        """Set this place as unvisited."""
        self.is_visited = False

    def is_important(self) -> bool:
        """
        Check if the place is considered important.

        A place is important if its priority is 2 or less.
        """
        return self.priority <= 2