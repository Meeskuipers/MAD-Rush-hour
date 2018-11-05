"""
Mees Kuipers
11288477

This class is used to make a room and checks if every value is in the room
"""
from inventory import Inventory


class Room(object):
    """
    Representation of a room in Adventure
    """
    # This are the values that every room needs

    def __init__(self, id, name, description):
        """
        Initialize a Room
        give it an id, name and description
        """
        self.id = id
        self.name = name
        self.description = description
        # The dictionary of the room is empty cause this is appended later,
        # after the room is already made
        self.dictionary = {}
        # The inventory of the room is made in inventory()
        self.inventory = Inventory()

    # Checks if the given command is valid
    def boolean(self, direction):
        """
        gives a boolean
        checks wether the input is valid
        """
        if direction in self.dictionary:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}{self.description}{self.inventory}\n"

