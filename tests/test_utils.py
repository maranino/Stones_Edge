import io
import unittest

from game.utils import load_characters_as
from game.character import Character
from game.player import Player


class TestUtils(unittest.TestCase):
    def test_load_empty_characters(self):
        file = io.StringIO('[]')
        characters = load_characters_as(file, Character)
        self.assertEqual(characters, [])


    def test_load_players(self):
        # mocking up a test file to read from
        file_content = '''[{
            "name": "John Wick",
            "hp": 10,
            "damage": 10,
            "magic": 2,
            "luck": 2,
            "job": "Warrior",
            "inventory": {
                "armor": "Bulletproof Suit",
                "weapon": "Dragons Breath Shotgun",
                "hp_potion": 2,
                "mp_potion": 1,
                "drops": "",
                "gathers": "",
                "gift": ""
            }
        }]
        '''
        file = io.StringIO(file_content)
        # Expecting a List of (Player) character(s)
        characters = load_characters_as(file, Player)

        self.assertEqual(len(characters), 1)
        john = characters[0]
        # character object type checks
        self.assertIsInstance(john, Player)
        self.assertIsInstance(john, Character)
        # character attribute value checks
        self.assertEqual(john.hp, 10)
        self.assertEqual(john.damage, 10)
        self.assertEqual(john.magic, 2)
        self.assertEqual(john.luck, 2)
        self.assertEqual(john.job, 'Warrior')
        # character inventory value checks
        self.assertEqual(john.inventory.armor, 'Bulletproof Suit')
        self.assertEqual(john.inventory.weapon, 'Dragons Breath Shotgun')
        self.assertEqual(john.inventory.hp_potion, 2)
        self.assertEqual(john.inventory.mp_potion, 1)
        self.assertEqual(john.inventory.drops, '')
        self.assertEqual(john.inventory.gathers, '')
        self.assertEqual(john.inventory.gift, '')