import unittest
from game.monster import Monster


class TestMonster(unittest.TestCase):
    def setUp(self):
        self.monster_data = {
            "name": "Goblin",
            "hp": 50,
            "damage": 8,
            "magic": 0,
            "luck": 2,
            "drops": ["Gold", "Dagger"]
        }

    def test_monster_creation(self):
        monster = Monster(**self.monster_data)
        self.assertIsInstance(monster, Monster)
        self.assertEqual(monster.name, "Goblin")
        self.assertEqual(monster.hp, 50)
        self.assertEqual(monster.damage, 8)
        self.assertEqual(monster.magic, 0)
        self.assertEqual(monster.luck, 2)
        self.assertEqual(monster.drops, ["Gold", "Dagger"])


if __name__ == "__main__":
    unittest.main()