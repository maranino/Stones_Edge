
from .character import Character
from .inventory import Inventory

class Player(Character):
    """Player represents a playable character type in the game."""
    def __init__(self, name, hp, damage, magic, luck, job, inventory):
        super().__init__(name, hp, damage, magic, luck)
        self.job = job
        self.inventory = Inventory(**inventory)

