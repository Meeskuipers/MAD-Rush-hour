"""
Mees Kuipers
11288477

Adventure is a game that only needed text to play
The adventure is a game that excist out of several rooms with all different
properties. The rooms are connected with each other and the player tries to find
the end of the game by putting the right commands. The commands are directions
or specific actions. These actions are for example taking/dropping items,
looking around in the room, a help function, a quit funciton or checking the
inventory of the player. If all the items are taken and the right room is
entered the player wins the game.
"""
from room import Room
from item import Item
from inventory import Inventory

import sys


class Adventure():
    """
    This is your Adventure game class. It should contains
    necessary attributes and methods to setup and play
    Crowther's text based RPG Adventure.
    """

    def __init__(self, game):
        """
        Create rooms and items for the appropriate 'game' version.
        """
        self.room_number = 0
        self.watch = []
        self.rooms = self.load_rooms(f"data/{game}Rooms.txt")
        self.items = self.load_items(f"data/{game}Items.txt")

    # Load all the rooms
    def load_rooms(self, filename):
        """
        Load rooms from filename.
        Returns a collection of Room objects.
        """
        with open(filename, "r") as file_room:
            # Rooms is the list were the id, the name, the description and the
            # directions of the room is in.
            self.roompjes = []
            # The dictionary makes sure that every direction is linked to an ID
            # number of another room
            # Checks every line
            for line in file_room:
                # Remove the \n
                line = line.strip()
                # Check if the line is a digit
                if line.isdigit():
                    id = line
                    # Skips a line
                    line = file_room.readline()
                    name = line
                    line = file_room.readline()
                    description = line
                    # room link all the information
                    room = Room(id, name, description)
                    # Saves all the information
                    self.roompjes.append(room)

                # Check if the line is all uppercase
                if line.isupper():
                    # Splits the words in the line in loose strings
                    line = line.split()
                    compas = line[0]
                    to_room = line[1]
                    # Add commands to the all excisting dictionaries
                    if compas in self.roompjes[-1].dictionary:
                        to_room_key = to_room
                        self.roompjes[-1].dictionary[compas].append(to_room_key)
                        self.roompjes[-1].inventory
                    # New dictionary if it is not already excisting
                    else:
                        to_room_key = [to_room]
                        self.roompjes[-1].dictionary[compas] = to_room_key
                        self.roompjes[-1].inventory
            # Is the current_room for the firs time
            self.current_room = self.roompjes[self.room_number]

    # Load all the items to the specific rooms
    def load_items(self, filename):
        with open(filename, "r") as file_item:
            # makes an empty item list
            self.item_list = []
            self.inventory_player = Inventory()
            for line in file_item:
                line = line.strip()
                # Checks if the line is upper
                if line.isupper():
                    name_item = line
                    line = file_item.readline()
                    description_item = line.strip("\n")
                    line = file_item.readline()
                    initial_room_id_item = line
                    # This is the description of a whole item, including all the information
                    one_item = Item(name_item, description_item, initial_room_id_item)
                    item_to_room = int(one_item.initial_room_id_item) - 1
                    self.roompjes[item_to_room].inventory.add(one_item)

        return self.item_list

    def __str__(self):
        return f"{self.rooms}"

    def won(self):
        """
        Check if the game is won.
        Returns a boolean.
        """
        # Returned True if the Victory is found en end the file
        if "Victory" in self.current_room.name:
            return True
        else:
            return False

    def move(self, direction):
        """
        Moves to a different room in the specified direction.
        """
        # self.watch is used to know if the new room is already entered. If it
        # is alreday entered only the name is printed, else the whole description
        self.watch.append(self.room_number)
        # The counter is used to break out of the for loop
        counter = 0
        # This function checks if the command that is given is already excisting
        if (self.current_room.boolean(direction)) == False:
            print("Invalid command")

        else:
            # Itterate over the whole dictionary and checks if there is a / in it
            for x in self.current_room.dictionary[direction]:
                # Breaks the loop if counter is 1 (see line 148 and 154)
                if counter == 1:
                    break
                if "/" in x:
                    # Splits the / out of the sentence
                    split = x.split("/")
                    room_number_if_item = split[0]
                    required_item = split[1]
                    # Itterate over all the items in the inventory of the player
                    for x in range(len(self.inventory_player.items)):
                        if required_item == self.inventory_player.items[x].name_item:
                            # This line finds the roomnumber of the room that
                            # the given command is linked to
                            # -1 is because start counting from 0
                            self.room_number = int(room_number_if_item) - 1
                            # The current room becomes the new room
                            self.current_room = self.roompjes[self.room_number]
                            # Checks if this room was already enterd (see line 122)
                            if self.room_number in self.watch:
                                description = self.current_room.description.strip()
                                # This statement makes sure that the curtain
                                # rooms are not printed
                                if "-----" != description:
                                    print(f"{self.current_room.name}{self.current_room.inventory}", end='')
                                counter = 1
                                break
                            else:
                                description = self.current_room.description.strip()
                                if "-----" != description:
                                    print(f"{self.current_room.description}{self.current_room.inventory}", end='')
                                counter = 1
                                break
                else:
                    self.room_number = int(x) - 1
                    self.current_room = self.roompjes[self.room_number]
                    if self.room_number in self.watch:
                        description = self.current_room.description.strip()
                        if "-----" != description:
                            print(f"{self.current_room.name}{self.current_room.inventory}", end='')
                    else:
                        description = self.current_room.description.strip()
                        if "-----" != description:
                            print(f"{self.current_room.description}{self.current_room.inventory}", end='')

        if "FORCED" in self.current_room.dictionary:
            for x in self.current_room.dictionary["FORCED"]:
                if "Victory" in x:
                    self.won()
                elif "0" in x:
                    sys.exit()
            self.move("FORCED")

    def play(self):
        """
        Play an Adventure game
        """
        print(f"Welcome, to the Adventure games.\n"
              "May the randomly generated numbers be ever in your favour.\n")
        print(f"{self.current_room.description}", end='')
        # Prompt the user for commands until they've won the game.
        while not self.won():
            command = input("> ").upper()
            if len(command) < 1:
                print("Invalid command")
            # Check if the command is a movement or not.
            elif command in ["NORTH", "N", "SOUTH", "S", "EAST", "E", "WEST", "W", "IN", "OUT", "DOWN", "D", "UP", "U", "JUMP", "WATER", "XYZZY", "PLUGH", "WAVE"]:
                if command == "N":
                    command = "NORTH"
                elif command == "S":
                    command = "SOUTH"
                elif command == "E":
                    command = "EAST"
                elif command == "W":
                    command = "WEST"
                elif command == "D":
                    command = "DOWN"
                elif command == "U":
                    command = "UP"
                self.move(command)
            elif command in ["HELP", "QUIT", "Q", "LOOK", "L", "INVENTORY", "I"]:
                if command == "Q":
                    command = "QUIT"
                elif command == "L":
                    command = "LOOK"
                elif command == "I":
                    command = "INVENTORY"
                self.add_command(command)
            else:
                command = command.split()
                if command[0] == "TAKE" and len(command) is 2:
                    self.add_item(command[1])
                elif command[0] == "DROP" and len(command) is 2:
                    self.drop_item(command[1])
                else:
                    print("Invalid command")
    # If the command is a help, quit of inventory this function will do the
    # following

    def add_command(self, additional):
        if additional == "HELP":
            # Opens the help.txt en print every line
            print("""You can move by typing directions such as EAST/WEST/IN/OUT
QUIT quits the game.
HELP prints instructions for the game.
INVENTORY lists the item in your inventory.
LOOK lists the complete description of the room and its contents.
TAKE <item> take item from the room.
DROP <item> drop item from your inventory.""")
        # exit the program
        elif additional == "QUIT":
            print("Thanks for playing!")
            exit()
        # shows the inventory of the player
        elif additional == "INVENTORY":
            if str(self.inventory_player) == "":
                print("Your inventory is empty.")
            else:
                print(f"{self.inventory_player}")
        else:
            print(f"{self.current_room.description}{self.current_room.inventory}")

    # This function changes the item from inventory
    def add_item(self, additional_item):
        # Checks all the items in the inventory of the current room by
        # itterating over all the items in the room
        for x in range(len(self.current_room.inventory.items)):
            # If the item is in the room, the item is added to the inventory
            # of the player and removed from the inventory of the room
            if additional_item == self.current_room.inventory.items[x].name_item:
                self.inventory_player.add(self.current_room.inventory.items[x])
                self.current_room.inventory.remove(self.current_room.inventory.items[x])
                print(f"{additional_item} taken")
                break
        else:
            print("No such item")

    # This function does the same thing ass add_item but then in opposite
    # direction
    def drop_item(self, additional_item):
        for x in range(len(self.inventory_player.items)):
            if additional_item == self.inventory_player.items[x].name_item:
                print(f"{additional_item} dropped")
                self.current_room.inventory.add(self.inventory_player.items[x])
                self.inventory_player.remove(self.inventory_player.items[x])
                break
        else:
            print("No such item")


if __name__ == "__main__":
    adventure = Adventure("Crowther")
    adventure.play()