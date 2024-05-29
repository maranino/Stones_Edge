import random
from datetime import date

from screens import characterScreen, locationsScreen, travelersScreen
from dialogue import intro, traveler_encounter, deny_traveler_encounter, game_lost
from art import mountains, forest, desert, swamps, gameOver, cross, diceArt, youWin


class Characters:
    '''parent class for characters'''
    def __init__(self, name, hp, mp, damage, magic, magic_defense, luck):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.damage = damage
        self.magic = magic
        self.magic_defense = magic_defense
        self.luck = luck

class Inventory:
    '''This class is to define the inventory for each character'''

    def __init__(self, armor, weapon, hp_potion, mp_potion, drops, gathers, gift):
        self.armor = armor
        self.weapon = weapon
        self.hp_potion = hp_potion
        self.mp_potion = mp_potion
        self.drops = drops
        self.gathers = gathers
        self.gift = gift

kiri_inventory = Inventory('Pelt', 'Scythe', 40, 40, '', '', '')
mika_inventory = Inventory('Vest', 'Dagger', 40, 40, '', '', '')
rusty_inventory = Inventory('Crown', 'Saber', 40, 40, '', '', '')
ciel_inventory = Inventory('Shield', 'Broadsword', 40, 40, '', '', '')
class Character(Characters):
    '''This class is to define each character's name, hit point, attack damage and their job title'''

    def __init__(self, name, job, hp, mp, damage, magic, magic_defense, luck, inventory):
        self.job = job
        self.inventory = inventory
        super().__init__(name, hp, mp, damage, magic, magic_defense, luck)


kiri = Character('Kiri','farmer', 140, 100, 60, 'Earth', 50, 15, kiri_inventory)
mika = Character('Mika', 'merchant', 120, 110, 70, 'Lightning', 60, 25, mika_inventory)
rusty = Character('Rusty', 'prince', 130, 90, 80, 'Water', 40, 30, rusty_inventory)
ciel = Character('Ciel', 'knight', 120, 80, 70, 'Fire', 30, 20, ciel_inventory)

class Monsters(Characters):
    '''This class is to define each monster's name, hit points and attack damage'''

    def __init__(self, name, hp, damage, mp, magic, magic_defense, luck, drops):
        self.drops = drops
        super().__init__(name, hp, mp, damage, magic, magic_defense, luck)


serpent = Monsters('Serpent', 190, 30, 40, 'Earth', 50, 4, 'Scales')
hawk = Monsters('Hawk', 180, 40, 40, 'Wind', 50, 3, 'Feathers')
bear = Monsters('Bear', 220, 50, 50, 'Ice', 40, 2, 'Fur')
gator = Monsters('Gator', 200, 40, 30, 'Water', 30, 6, 'Teeth')

class Traveler:
    '''This class is to specify the details of the traveler'''
    def __init__(self, name, gift):
        self.name = name
        self.gift = gift

tristan = Traveler('Tristan', 'corn dolly')
mark = Traveler('Mark', 'amulet')
trinity = Traveler('Trinity', 'voodoo doll')
juni = Traveler('Juni', 'seer stone')

class Locations():
    '''This class is to define each location's direction, terrain, 
    the traveler, and the cover, trap and monument found in the story'''

    def __init__(self, direction, terrain, traveler, cover, trap, monument):
        self.direction = direction
        self.terrain = terrain
        self.traveler = traveler
        self.cover = cover
        self.trap = trap
        self.monument = monument

east = Locations('east', 'forest', tristan.name, 'tree', 'into a pit of spikes', 'totem pole')
west = Locations('west', 'desert', mark.name, 'rock', 'into a pit of snakes', 'obelisk')
south = Locations('south', 'swamps', trinity.name, 'broken tree', 'into quicksand', 'tomb')
north = Locations('north', 'mountains', juni.name, 'boulder', 'off a cliff', 'temple')

beginning_date = date(1556, 6, 20)
early_death = date(1556, 6, 21)
game_date = date(1556, 6, 22)
trap_death = date(1556, 6, 23)
end_date = date(1556, 6, 24)

journey_time = {'journey1' : end_date.day - beginning_date.day,
               'journey2' : early_death.day - beginning_date.day,
               'journey3' : game_date.day - beginning_date.day,
               'journey4' : trap_death.day - beginning_date.day
               }

def gameplay():
    '''Play the game'''
    while True:
        while True:
            # Choose the Character:
            characterScreen()
            choice = input("""
                 Which character do you choose? """).lower()

            if choice == "1" or choice == "kiri":
                character = kiri
                inventory = kiri_inventory
                break

            elif choice == "2" or choice == "mika":
                character = mika
                inventory = mika_inventory
                break

            elif choice == "3" or choice == "rusty":
                character = rusty
                inventory = rusty_inventory
                break

            elif choice == "4" or choice == "ciel":
                character = ciel
                inventory = ciel_inventory
                break

            elif choice == "5" or choice == "exit":
                print("Goodbye!")
                exit()

            else:
                print("Invalid entry, try again!")

        intro(character, inventory, beginning_date)

        while True:
            # Choose the Location
            locationsScreen()
            choice = input("""
                   Which direction will you go? """).lower()

            if choice == "mountains" or choice == "north":
                location = north
                monster = hawk
                mountains()
                break

            elif choice == "forest" or choice == "east":
                location = east
                monster = bear
                forest()
                break

            elif choice == "desert" or choice == "west":
                location = west
                monster = serpent
                desert()
                break

            elif choice == "swamps" or choice == "south":
                location = south
                monster = gator
                swamps()
                break

            elif choice == "5" or choice == "exit":
                print(f"Goodbye {character.name}!")
                exit()

            else:
                print("Invalid entry, try again!")
        print(f"""
            You have chosen the {location.terrain} to the {location.direction}.
        Only moments into your adventure you are attacked by a {monster.name}!

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->   
    """)
        while True:
            # Monster Battle
            monster.hp -= character.damage
            print(f"""
                {character.name} attacks the {monster.name}!
                The {monster.name}'s hit points are now: {str(monster.hp)}
        """)
            if monster.hp > 0:
                character.hp -= monster.damage
                print(f"""
                    The {monster.name} strikes back at {character.name}!
                    {character.name}'s hit points are now: {str(character.hp)}
        """)
            if character.hp <= 0:
                print(f"""
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                {character.name} has lost the battle.
            {early_death.strftime('%B')} {early_death.day}, {early_death.year} is when your story ends...
                Your journey lasted {journey_time['journey2']} day.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
    """)
                cross()
                replay()
            if monster.hp <= 0:
                print(f"""
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                    The {monster.name} has lost the battle.
                       You emerge victorious!
            Beaten and battered from the intense battle 
                    you look for a place to rest.
    You find a large {location.cover} to to hide behind as you recover.
                Several hours pass then you are awoken 
                by the sounds of a traveler passing by.
                You decide whether or not to approach 
                    the traveler for information.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
            """)
                break
        while True:
            # Approach Traveler?
            travelersScreen()
            choice = input("""
                  Will you approach the Traveler? """).lower()
            if choice == "yes" or choice == "y":
                traveler_encounter(location, monster)
                # Game
                dice = random.randint(1, 6)
                print(f"""
            You roll the dice... it lands on {dice}!

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
    """)
                diceArt()
                if dice <= 3:
                    prizes = [f"""

                     THE RARE JEWEL!

                      .     '     ,
                        _________
                     _ /_|_____|_\ _
                       '. \   / .'
                         '.\ /.'
                           '.'

        You have succeeded in your adventure on {game_date.strftime('%B')} {game_date.day}, {game_date.year}!
                 Your journey lasted {journey_time['journey3']} days.
        


                    """, youWin(), f"""

                      An old coin? 
    {location.traveler} places it into your hand and you evaluate it.
                Why would I want such a thing? 
            As you look up {location.traveler} is gone...
                    Something is off... 
        You reach for your coin bag and it's gone!
            You have been tricked by {location.traveler}!
                You are wounded, starved 
        and now you don't even have money to buy food!
        You don't have the strength to hunt anything, 
          if they are anything like that {monster.name}!
        You are forced to return home on {game_date.strftime('%B')} {game_date.day}, {game_date.year}
               with shame of your failure!
               Your journey lasted {journey_time['journey3']} days.
                    
                    """]
                    prize_won = random.choice(prizes)
                    print(f"""
                     You have won... 
                  {prize_won}""")
                    replay()

                else:
                   game_lost(location)
                chance = [f"There are no hints or clues at this {location.monument}!", f"The jewel you look for has already been taken by {location.traveler}!"]
                clue = random.choice(chance)
                print(f"""
      There was always a chance that the rumors weren't true.
        This moment will determine the fate of my adventure!
        If I get no new leads here, then I must return home.
      As you inspect the {location.monument}, you find a hand written note.
                            It says... 
        {clue}

                Your Adventure Ends on {end_date.strftime('%B')} {end_date.day}, {end_date.year}...
                   Your journey lasted {journey_time['journey1']} days.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->    
                """)
                replay()

            elif choice == "no" or choice == "n":
                deny_traveler_encounter(monster, location, trap_death, journey_time)
                cross()
                replay()

            elif choice == "exit":
                print(f"Goodbye {character.name}!")
                exit()
            else:
                print("Invalid entry, try again!")


# Code for replay the game
def replay():
    '''replay the game?'''
    play = input("""
                            Play again? """).lower()
    if play == "yes" or play == "y":
        gameplay()
    if play == "no" or play == "n":
        gameOver()
    quit()


gameplay()
