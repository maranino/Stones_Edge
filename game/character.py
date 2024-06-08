

class Character:
    """
    Character is a base character class for all characters in the game.
    """
    def __init__(self, name, hp, damage, magic, luck):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.magic = magic
        self.luck = luck

    def _take_damage(self, damage):
        """Private helper that side-effects character's hp attribute.
        NOTE: This should only be called within methods of this class.
        
        Args:
            damage: The amount of damage to apply to the character's hp.
        
        Returns:
            None
        """
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0 # ensure we don't go negative
            return

    def attack(self, other):
        """Attack another character (other) and deal damage.
        
        Args:
            other: The character to attack.
        
        Returns:
            None
        """
        # NOTE: could perform more complex attack logic/calculations
        # before passing to _take_damage.

        # call the other characters _take_damage method to apply damage
        other._take_damage(self.damage)
