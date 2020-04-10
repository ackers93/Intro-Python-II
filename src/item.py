class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take(self):
        return f'You have aquired {self.name}'

    def drop(self):
        return f'You dropped {self.name}'
