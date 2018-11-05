"""
Mees Kuipers
11288477

This class is for all the items
"""


class Item(object):
    # In the init there are all the variables that is needed to specifie an item
    def __init__(self, name, description, initial_room_id):
        self.name_item = name
        self.description_item = description
        self.initial_room_id_item = initial_room_id

    def __str__(self):
        return f"{self.name_item}: {self.description_item}"

