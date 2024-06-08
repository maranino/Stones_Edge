import unittest

from game.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        inventory = {
            "armor": "Pelt",
            "weapon": "Scythe",
            "hp_potion": 40,
            "mp_potion": 40,
            "drops": "",
            "gathers": "",
            "gift": ""
        }
        self.player_data = {
            "name": "Hero",
            "hp": 100,
            "damage": 15,
            "magic": 10,
            "luck": 5,
            "job": "Warrior",
            "inventory": inventory
        }
        

    def test_player_creation(self):
        player = Player(**self.player_data)
        self.assertIsInstance(player, Player)
        self.assertEqual(player.name, "Hero")
        self.assertEqual(player.hp, 100)
        self.assertEqual(player.damage, 15)
        self.assertEqual(player.magic, 10)
        self.assertEqual(player.luck, 5)
        self.assertEqual(player.job, "Warrior")
        self.assertEqual(player.inventory.armor, "Pelt")


if __name__ == "__main__":
    unittest.main()