import random
import global_vars as gv
from item import Item


class ItemHandler:

    def __init__(self):
        # start values
        self.timer = 0
        self.creation_time = 5

        # parameters
        self.types = list(gv.types.keys())
        self.creation_time_range = (2, 10)  # min, max
        self.lifetime_range = (10, 20)  # min, max

    def update(self):
        self.timer += gv.elapsed_time

        # item updates
        for i in reversed(gv.items):
            i.update()

        # item creation
        if self.timer > self.creation_time:
            item_type = random.choice(self.types)
            life_time = random.randint(*self.lifetime_range)
            gv.items.append(Item(item_type, life_time))
            self.timer = 0
            self.creation_time = random.randint(*self.creation_time_range)


