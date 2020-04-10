# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, description):
        self.name = room_name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def display_room_items(self):
        if len(self.items) == 0:
            print("There are no items in this room")
        else:
            print('The room contains: ')
            for item in self.items:
                print(item.name)
