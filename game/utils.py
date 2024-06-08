import json

from .character import Character


def load_characters_as(file, cls=Character):
    """Load JSON character data from a file and
    return it as a list of instances of cls.

    Usage:
        # NOTE: assuming relative path from stones_edge.py
        
        with open('data/players.json', 'r') as file:
            # Load the characters as Player instances.
            all_players = load_characters_as(file, cls=Player)
            all_monsters = load_characters_as(file, cls=Monster)
    
    Args:
        file: A file-like object containing JSON data.
        cls: The class to instantiate for each character.
    
    Returns:
        A list of instances of the type of cls.
    """
    characters = []
    try:
        data = json.load(file)
    except json.JSONDecodeError:
        return characters
    
    for character in data:
        characters.append(cls(**character))
    return characters
