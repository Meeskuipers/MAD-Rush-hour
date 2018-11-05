"""
Mees Kuipers
11288477

This function import the items of a room
It can remove and add the items to the inventory
"""
from item import Item


class Inventory(object):
    def __init__(self):
        self.items = []

    # Add the items to the inventory
    def add(self, item):
        self.items.append(item)

    # Remove the items from the inventory
    def remove(self, item):
        self.items.remove(item)

    def __str__(self):
        if len(self.items) is not 0:
            return '\n'.join(map(str, self.items)) + "\n"
        else:
            return ("")