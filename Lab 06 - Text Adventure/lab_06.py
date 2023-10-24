class Room:
    def __init__(self, description="", north=None, east=None, south=None, west=None):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def print_introduction():
    print("""
Welcome to the Temple of Entropy!

You find yourself standing at the entrance of an old and mysterious temple. The air is filled
with an eerie silence, and the dim torch light casts shadows on the worn-out walls. As you enter the
grand hall, you notice several doorways leading to different rooms. Adventure awaits you as you
explore the secrets hidden within this ancient place of worship.

Commands:
- Type 'north' or 'n' to go north.
- Type 'east' or 'e' to go east.
- Type 'south' or 's' to go south.
- Type 'west' or 'w' to go west.
- Type 'quit' to exit the game.
""")


def main():
    room_list = []

    room = Room(
        "You find yourself in the grand hall. An old fireplace crackles. There are doorways to the north and east.", 3,
        1, None, None)
    room_list.append(room)
    # room 1

    room = Room(
        "You are in a long stone hallway. There are doorways to the north, east, and west.", 4, 2, None, 0)
    room_list.append(room)
    # room 2

    room = Room(
        "You enter the kitchen. The smell of rotten meat fills the air. There are doorways to the "
        "north and west.", 5, None, None, 1)
    room_list.append(room)
    # room 3

    room = Room(
        "You step into the bathroom. There is dried blood here. There are doorways to the east and south",
        None, 4, 0, None)
    room_list.append(room)
    # room 4

    room = Room(
        "Welcome to the bedroom. A regal bed dominates the room. This room is surprisingly clean compared to "
        "the rest of the temple. There are doorways in all directions.", 6, 5, 1, 3)
    room_list.append(room)
    # room 5

    room = Room(
        "The pantry is messy and smells funny. There are doorways to the west and south.", None, None, 2, 4)
    room_list.append(room)
    # room 6

    room = Room(
        "You enter a crowded armory. Racks line the walls filled to the brim with medieval weaponry. There is a"
        "doorway to the south.", None, None, 4, None)
    room_list.append(room)
    # room 7

    current_room = 0

    done = False

    while not done:
        print("\n")  # blank space
        print(room_list[current_room].description)

        user_input = input("What do you want to do? ")

        if user_input.lower() in ["n", "north"]:
            next_room = room_list[current_room].north
            if next_room is not None:
                current_room = next_room
            else:
                print("You can't go that way.")
        elif user_input.lower() in ["e", "east"]:
            next_room = room_list[current_room].east
            if next_room is not None:
                current_room = next_room
            else:
                print("You can't go that way.")
        elif user_input.lower() in ["s", "south"]:
            next_room = room_list[current_room].south
            if next_room is not None:
                current_room = next_room
            else:
                print("You can't go that way.")
        elif user_input.lower() in ["w", "west"]:
            next_room = room_list[current_room].west
            if next_room is not None:
                current_room = next_room
            else:
                print("You can't go that way.")
        elif user_input.lower() == "quit":
            done = True
        else:
            print("I don't understand that command.")


print_introduction()

if __name__ == "__main__":
    main()
