import unittest
from game.character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character_data = {
            "name": "Test Character",
            "hp": 100,
            "damage": 10,
            "magic": 5,
            "luck": 3,
        }

    def test_character_creation(self):
        character = Character(**self.character_data)
        self.assertEqual(character.name, "Test Character")
        self.assertEqual(character.hp, 100)
        self.assertEqual(character.damage, 10)
        self.assertEqual(character.magic, 5)
        self.assertEqual(character.luck, 3)


if __name__ == "__main__":
    unittest.main()