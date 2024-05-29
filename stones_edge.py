import random
from datetime import date

from screens import characterScreen, locationsScreen, travelersScreen
from dialogue import intro
from art import castle, mountains, forest, desert, swamps, gameOver, cross, diceArt, youWin


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

kiri_inventory = Inventory('pelt', 'scythe', 40, 40, '', '', '')
mika_inventory = Inventory('vest', 'dagger', 40, 40, '', '', '')
rusty_inventory = Inventory('crown', 'saber', 40, 40, '', '', '')
ciel_inventory = Inventory('shield', 'broadsword', 40, 40, '', '', '')
class Character(Characters):
    '''This class is to define each character's name, hit point, attack damage and their job title'''

    def __init__(self, name, job, hp, mp, damage, magic, magic_defense, luck, inventory):
        self.job = job
        self.inventory = inventory
        super().__init__(name, hp, mp, damage, magic, magic_defense, luck)


kiri = Character('Kiri','farmer', 140, 100, 60, 'earth', 50, 15, kiri_inventory)
mika = Character('Mika', 'merchant', 120, 110, 70, 'lightning', 60, 25, mika_inventory)
rusty = Character('Rusty', 'prince', 130, 90, 80, 'water', 40, 30, rusty_inventory)
ciel = Character('Ciel', 'knight', 120, 80, 70, 'fire', 30, 20, ciel_inventory)

class Monsters(Characters):
    '''This class is to define each monster's name, hit points and attack damage'''

    def __init__(self, name, hp, damage, mp, magic, magic_defense, luck, drops):
        self.drops = drops
        super().__init__(name, hp, mp, damage, magic, magic_defense, luck)


serpent = Monsters('Serpent', 190, 30, 40, 'earth', 50, 4, 'scales')
hawk = Monsters('Hawk', 180, 40, 40, 'wind', 50, 3, 'feathers')
bear = Monsters('Bear', 220, 50, 50, 'ice', 40, 2, 'fur')
gator = Monsters('Gator', 200, 40, 30, 'water', 30, 6, 'teeth')

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

beginningDate = date(1556, 6, 20)
earlyDeath = date(1556, 6, 21)
gameDate = date(1556, 6, 22)
trapDeath = date(1556, 6, 23)
endDate = date(1556, 6, 24)

journeyTime = {'journey1' : endDate.day - beginningDate.day,
               'journey2' : earlyDeath.day - beginningDate.day,
               'journey3' : gameDate.day - beginningDate.day,
               'journey4' : trapDeath.day - beginningDate.day
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
                break

            elif choice == "2" or choice == "mika":
                character = mika
                break

            elif choice == "3" or choice == "rusty":
                character = rusty
                break

            elif choice == "4" or choice == "ciel":
                character = ciel
                break

            elif choice == "5" or choice == "exit":
                print("Goodbye!")
                exit()

            else:
                print("Invalid entry, try again!")

        print(f"""
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                        You have chosen {character.name}
                        Your Hp is: {character.hp}
                        Your damage is: {character.damage}
        
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                    The date is {beginningDate.strftime('%B')} {beginningDate.day}, {beginningDate.year}
                        You are named {character.name},
            a {character.job} from the Royal City of Stone's Edge.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
        """)
        castle()
        intro()
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
            {earlyDeath.strftime('%B')} {earlyDeath.day}, {earlyDeath.year} is when your story ends...
                Your journey lasted {journeyTime['journey2']} day.

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
                print(f"""
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

        You emerge from the {location.cover} and introduce yourself.
                They says their name is {location.traveler}.
        The traveler sees you are wounded and asks... 
            why you are outside the walls of the Royal City.
            You tell {location.traveler} of the {monster.name} attack
                    and how you barely escaped...
            Then you tell them of the rumor you heard 
                and ask if they had known anything.
                        {location.traveler} says they have,
            but first you must win a game of their choice.
                            You agree.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
                
        {location.traveler} tells you, you will roll a single dice...
                    If it lands on 3 or under, 
            I will give you what is in my pocket...
    If it lands on a 4 or more then you will be on your own!
            You tell {location.traveler} that this sounds fair enough.
                {location.traveler} then hands you the single dice.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
    """)
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

        You have succeeded in your adventure on {gameDate.strftime('%B')} {gameDate.day}, {gameDate.year}!
                 Your journey lasted {journeyTime['journey3']} days.
        


                    """,youWin(), f"""

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
        You are forced to return home on {gameDate.strftime('%B')} {gameDate.day}, {gameDate.year}
               with shame of your failure!
               Your journey lasted {journeyTime['journey3']} days.
                    
                    """]
                    prize_won = random.choice(prizes)
                    print(f"""
                     You have won... 
                  {prize_won}""")
                    replay()

                else:
                    print(f"""
                        Sorry you lose... 
        {location.traveler} says they cannot help you, a deal is a deal.
                        It is the truth... 
    I suppose I will look further in the {location.terrain} for clues.
                You say your farewells and continue on.
                You go deeper into the {location.terrain}...
        Back home you heard that there was a {location.monument}
                that held a clue of the jewels location!
                If you could just find this, 
            surely you will find what you are looking for...
    You have a crude map you had drawn up back home, 
        you pull it out and see if you could find your way...
        
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                You stumble around for a while 
                and almost fall {location.trap}!
            Thankfully you saw it last minute! 
        Being a little more cautious now you continue on...
            As the sun starts to set you begin to worry
                and look for a place to camp.
         You see a similar {location.cover} like before
              and figure since it worked last time,
        you should try hiding in a spot like that again!
    You get closer to look around and make sure it's all clear.
          As you peak your head around the {location.cover}
         you see the {location.monument} you were looking for!
                 You quickly move towards it 
              to look for the clue you heard of!

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->           
        """)
                chance = [f"There are no hints or clues at this {location.monument}!", f"The jewel you look for has already been taken by {location.traveler}!"]
                clue = random.choice(chance)
                print(f"""
      There was always a chance that the rumors weren't true.
        This moment will determine the fate of my adventure!
        If I get no new leads here, then I must return home.
      As you inspect the {location.monument}, you find a hand written note.
                            It says... 
        {clue}

                Your Adventure Ends on {endDate.strftime('%B')} {endDate.day}, {endDate.year}...
                   Your journey lasted {journeyTime['journey1']} days.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->    
                """)
                replay()

            elif choice == "no" or choice == "n":
                print(f"""
                
            You stay hidden and let the traveler pass...
            You never know if someone is friendly or not!
                You do not have the strength to fight 
                after that battle with the {monster.name}!
            Instead you go deeper into the {location.terrain}...
            Back home you heard that there was a {location.monument}
                that held a clue of the jewels location!
                    If you could just find this, 
            surely you will find what you are looking for...
        You have a crude map you had drawn up back home, 
        you pull it out and see if you could find your way...
                    You slowly step forward as you 
            try to trace your steps from the city...
                    Suddenly!! You step {location.trap}!!

                  You have died on {trapDeath.strftime('%B')} {trapDeath.day}, {trapDeath.year}!
                  Your journey lasted {journeyTime['journey4']} days.
                                                        
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->        
        """)
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
