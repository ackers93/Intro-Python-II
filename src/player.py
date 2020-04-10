# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        if new_room == None:
            print("Choose a different direction")
        elif new_room is not None:
            self.current_room = new_room
            print("Your current location is:", self.current_room.name)
            print(self.current_room.description)
            self.current_room.display_room_items()

    def show_room(self):
        print(self.current_room.description)

    def inventory_list(self):
        print('You have obtained so far: ')
        for item in self.items:
            print(item.name)

    def take(self, item):
        for i in self.current_room.items:
            if i.name == item:
                self.items.append(i)
                self.current_room.items.remove(i)
                print('You have added an item to your inventory')
            else:
                print("This room is empty")

    def drop(self, item):
        for i in self.items:
            if i.name == item:
                self.current_room.items.append(i)
                self.items.remove(i)
                print('You have dropped the item')
            else:
                print('You dont have this item in your inventory')
