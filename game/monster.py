import random

from .character import Character


class Monster(Character):
    """Monster represents a non-playable enemy character type in the game."""
    MONSTERS = [
        {'name': 'Goblin', 'hp': 50, 'damage': 10, 'magic': 0, 'magic_defense': 5, 'luck': 5},
        {'name': 'Orc', 'hp': 80, 'damage': 15, 'magic': 5, 'magic_defense': 10, 'luck': 10},
        {'name': 'Dragon', 'hp': 200, 'damage': 25, 'magic': 20, 'magic_defense': 20, 'luck': 5}
    ]

    def __init__(self, name, hp, damage, magic, luck, drops):
        super().__init__(name, hp, damage, magic, luck)
        self.drops = drops

    @staticmethod
    def generate_monster():
        """Generate a random monster from the list of predefined MONSTERS."""
        choice = random.choice(Monster.MONSTERS)
        return Monster(**choice)
