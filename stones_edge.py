import random

# Characters
kiri = "Kiri"
kiri_hp = 140
kiri_damage = 60
kiri_job = "farmer"

mika = "Mika"
mika_hp = 120
mika_damage = 70
mika_job = "merchant"

rusty = "Rusty"
rusty_hp = 130
rusty_damage = 80
rusty_job = "prince"

ciel = "Ciel"
ciel_hp = 120
ciel_damage = 70
ciel_job = "knight"

# Monsters
serpant = "Serpant"
serpant_hp = 190
serpant_damage = 30

hawk = "Hawk"
hawk_hp = 180
hawk_damage = 40

bear = "Bear"
bear_hp = 220
bear_damage = 50

gator = "Gator"
gator_hp = 200
gator_damage = 40

# Travelers
traveler_east = "Tristan"
traveler_west = "Mark"
traveler_south = "Trinity"
traveler_north = "Juni"

# Locations
forrest, east = "forrest", "east"
desert, west = "desert", "west"
swamps, south = "swamps", "south"
mountains, north = "mountains", "north"

# Cover
tree = "tree"
rock = "rock"
broken_tree = "broken tree"
boulder = "boulder"

# Trap
pit = "a into pit of spikes"
den = "a into den of snakes"
quicksand = "into quicksand"
cliff = "off a cliff"

# Monument
totem = "totem pole"
obelisk = "obelisk"
tomb = "tomb"
temple = "temple"

def gameplay():
    while True:
        while True:
            # Choose the Character:
            print("""

                     === Character List ===           
            -------------------------------------------
            | 1.    Kiri       | 2.      Mika         |
            -------------------------------------------
            | 3.    Rusty      | 4.      Ciel         |
            -------------------------------------------
            |              5.   Exit                  |
            -------------------------------------------
            """)
            choice = input("""
                 Which character do you choose? """).lower()

            if choice == "1" or choice == "kiri":
                character = kiri
                my_hp = kiri_hp
                my_damage = kiri_damage
                my_job = kiri_job
                break

            elif choice == "2" or choice == "mika":
                character = mika
                my_hp = mika_hp
                my_damage = mika_damage
                my_job = mika_job
                break

            elif choice == "3" or choice == "rusty":
                character = rusty
                my_hp = rusty_hp
                my_damage = rusty_damage
                my_job = rusty_job
                break

            elif choice == "4" or choice == "ciel":
                character = ciel
                my_hp = ciel_hp
                my_damage = ciel_damage
                my_job = ciel_job
                break

            elif choice == "5" or choice == "exit":
                print("Goodbye!")
                exit()
            
            else:
                print("Invalid entry, try again!")
            

        print(f"""
        
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                    You have chosen {character}
                    Your Hp is: {my_hp}
                    Your damage is: {my_damage}
        
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                    You are named {character}...
        a {my_job} from the Royal City of Stone's Edge.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
        
                                       o
                               _---|         _ _ _ _ _
                            o   ---|     o   ]-I-I-I-[
           _ _ _ _ _ _  _---|      | _---|    \ ` ' /
           ]-I-I-I-I-[   ---|      |  ---|    |.   |
            \ `   '_/       |     / \    |    | /^\|
             [*]  __|       ^    / ^ \   ^    | |*||
             |__   ,|      / \  /    `\ / \   | ===|
          ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
          I_I__I_I__I_I  (====(_________)___|_|____|____
          \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_|
           |[]      '|   | []  |`__  . [  \-\--|-|--/-/
           |.   | |' |___|_____I___|___I___|---------|
          / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] |
         <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  
         | []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===>
         | []| ` |   |/ / / / / \ \ \ \ \.||__.....|[] |
         <===>     ' ||||| |   |   | ||||.||  []   <===>
          \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/
           |      . _||||| |   |   | ||||.|| |     | |
        ../|' v . | .|||||/____|____\|||| /|. . | . .|
        .|//\............/...........\........../../ | 
        
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

        There has been a rumor floating around town...    
        of a rare jewel the King lost on his last journey.
                        Problem is...    
        the details seem to change depending on who you ask.
        You have four different options of where to go...    
                    Which will you choose? 

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
        """)
        while True:
            # Choose the Location
            print("""
                        === Location list ===           
            -------------------------------------------
            |  North - Mountains  |   East - Forrest   |
            -------------------------------------------
            |    West - Desert    |   South - Swamps   |
            -------------------------------------------
            |              5.   Exit                   |
            -------------------------------------------
            """)
            choice = input("""
                   Which direction will you go? """).lower()

            if choice == "mountains" or choice == "north":
                location = mountains
                direction = north
                monster = hawk
                monster_hp = 180
                monster_damage = 40
                Traveler = traveler_north
                cover = boulder
                trap = cliff
                monument = temple
                print(""" 

                                       /\ 
                                  /\  /  \ 
                           /\    // \// ^ \        /\ 
                          // \  ///\//   ^ \  /\  // \ 
             /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \ 
            / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \ 
           /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
          /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\ 
         / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\ 
        / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\ 
       /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\ 
      /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\       
     / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |           
    / ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooo  
    ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            
                """)
                break

            elif choice == "forrest" or choice == "east":
                location = forrest
                direction = east
                monster = bear
                monster_hp = 220
                monster_damage = 50
                Traveler = traveler_east
                cover = tree
                trap = pit
                monument = totem
                print("""
 
         ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
        /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\ 
        /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\ 
        /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\ 

                """)

                break

            elif choice == "desert" or choice == "west":
                location = desert
                direction = west
                monster = serpant
                monster_hp = 190
                monster_damage = 30
                Traveler = traveler_west
                cover = rock
                trap = den
                monument = obelisk
                print(""" 

               ,,                               .-.
              || |                               ) )
              || |   ,                          '-'
              || |  | |
              || '--' |
        ,,    || .----'
       || |   || |
       |  '---'| |
       '------.| |                                  _____
       ((_))  || |      (  _                       / /|\ \ 
       (o o)  || |      ))("),                    | | | | |
    ____\_/___||_|_____((__^_))____________________\_\|/_/__

                """)
                break

            elif choice == "swamps" or choice == "south":
                location = swamps
                direction = south
                monster = gator
                monster_hp = 200
                monster_damage = 50
                Traveler = traveler_south
                cover = broken_tree
                trap = quicksand
                monument = tomb
                print("""

                      __..-:'':__:..:__:'':-..__
                  _.-:__:.-:'':  :  :  :'':-.:__:-._
                .':.-:  :  :  :  :  :  :  :  :  :._:'.
             _ :.':  :  :  :  :  :  :  :  :  :  :  :'.: _
            [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
            [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
   :::::::::[ ]:__:__:__:__:__:__:__:__:__:__:__:__:__:[ ]:::::::::::
   !!!!!!!!![ ]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![ ]!!!!!!!!!!!
   ^^^^^^^^^[ ]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[ ]^^^^^^^^^^^
            [ ]                                        [ ]
            [ ]                                        [ ]
            [ ]                                        [ ]
    ~~^_~^~/   \~^-~^~ _~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/   \~^ ~~_ ^

    """)

                break

            elif choice == "5" or choice == "exit":
                print(f"Goodbye {character}!")
                exit()

            else:
                print("Invalid entry, try again!")
        print(f"""
        
        You have chosen the {location} to the {direction}.
    Only moments into your adventure you are attacked by a {monster}!

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->   
    """)
        while True:
            # Monster Battle
            monster_hp = monster_hp - my_damage
            print(f"""
            {character} attacks the {monster}!
            The {monster}'s hitpoints are now: {str(monster_hp)}
        """)
            if monster_hp > 0:
                my_hp = my_hp - monster_damage
                print(f"""
                The {monster} strikes back at {character}!
                {character}'s hitpoints are now: {str(my_hp)}
        """)
            if my_hp <= 0:
                print(f"""
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                {character} has lost the battle.
                This is where your story ends...
                             __
                            /_/\/\  
                            \_\  /
                            /_/  \  
                            \_\/\ \   
                               \_\/

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
    """)
                replay() 
            if monster_hp <= 0:
                print(f"""
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                The {monster} has lost the battle.
                        You emerge victorious!
            Beaten and battered from the intense battle 
                    you look for a place to rest.
    You find a large {cover} to to hide behind as you recover.
                Several hours pass then you are awoken 
            by the sounds of a traveler passing by.
                You decide whether or not to approach 
                    the traveler for information.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
            """)
                break

        while True:
            # Approach Traveler?
            print("""
                    === Approach Traveler? ===        
            -------------------------------------------
            |         Yes         |         No         |
            -------------------------------------------
            |                   Exit                   |
            -------------------------------------------
            """)
            choice = input("""
                  Will you approach the Traveler? """).lower()

            if choice == "yes" or choice == "y":
                print(f"""
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

        You emerge from the {cover} and introduce yourself.
                They says their name is {Traveler}.
        The traveler sees you are wounded and asks... 
            why you are outside the walls of the Royal City.
            You tell {Traveler} of the {monster} attack 
                    and how you barely escaped...
            Then you tell them of the rumor you heard 
                and ask if they had known anthing.
                    {Traveler} says they have, 
            but first you must win a game of their choice.
                            You agree.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
                
        {Traveler} tells you, you will roll a single dice...
                If it lands on 3 or under, 
            I will give you what is in my pocket...
    If it lands on a 4 or more then you will be on your own!
        You tell {Traveler} that this sounds fair enough.
            {Traveler} then hands you the single dice.

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
    """)
                # Game
                dice = random.randint(1, 6)
                print(f"""
            You roll the dice... it lands on {dice}!
                          _______            
                        /\       \           
                       /()\   ()  \          
                      /    \_______\         
                      \    /()     /         
                       \()/   ()  /          
                        \/_____()/      

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
    """)
                if dice <= 3:
                    prizes = [f"""

                     **THE RARE JEWEL!

                      .     '     ,
                        _________
                     _ /_|_____|_\ _
                       '. \   / .'
                         '.\ /.'
                           '.'

            You have succeeded in your adventure!**

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
         __   __ _______ __   __    _     _ ___ __    _ __ 
        |  | |  |       |  | |  |  | | _ | |   |  |  | |  |
        |  |_|  |   _   |  | |  |  | || || |   |   |_| |  |
        |       |  | |  |  |_|  |  |       |   |       |  |
        |_     _|  |_|  |       |  |       |   |  _    |__|
          |   | |       |       |  |   _   |   | | |   |__ 
          |___| |_______|_______|  |__| |__|___|_|  |__|__|

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                    """, f"""

                    An old coin? 
    {Traveler} places it into your hand and you evaluate it.
                Why would I want such a thing? 
            As you look up {Traveler} is gone...
                    Something is off... 
        You reach for your coin bag and it's gone!
            You have been tricked by {Traveler}!
                You are wounded, starved 
        and now you don't even have money to buy food!
        You don't have the strength to hunt anything, 
        if they are anything like that {monster}!
            You are forced to return home, 
            with shame of your failure!
                    
                    """]
                    prize_won = random.choice(prizes)
                    print(f"""
                     You have won... 
                  {prize_won}""")
                    replay()

                else:
                    print(f"""
                        Sorry you lose... 
        {Traveler} says they cannot help you, a deal is a deal.
                        It is the truth... 
    I suppose I will look further in the {location} for clues.
                You say your farewells and continue on.
                You go deeper into the {location}...
        Back home you heard that there was a {monument} 
                that held a clue of the jewels location!
                If you could just find this, 
            surely you will find what you are looking for...
    You have a crude map you had drawn up back home, 
        you pull it out and see if you could find your way...
        
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                You stumble around for a while 
                and almost fall {trap}! 
            Thankfully you saw it last minute! 
        Being a little more cautious now you continue on...
            As the sun starts to set you begin to worry
                and look for a place to camp.
                You see a similar {cover} like before
                and figure since it worked last time,
        you should try hiding in a spot like that again!
    As you get closer you look around to make sure it's all clear.
            As you peak your head around the {cover} 
            you see the {monument} you were looking for!
                    You quickly move towards it 
                to look for the clue you heard of!

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->           
        """)
                chance = [f"There are no hints or clues at this {monument}!", f"The jewel you look for has already been taken by {Traveler}!"]
                clue = random.choice(chance)
                print(f""" 
        There was always a chance that the rumors weren't true.
        This moment will determine the fate of my adventure!
        If I get no new leads here, then I must return home.
                    As you inspect the {monument}, 
                    you find a hand written note...
                            It says... 
        {clue}

                    Your Adventure Ends Here.....

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->    
                """)
                replay()

            elif choice == "no" or choice == "n":
                print(f"""
                
            You stay hidden and let the traveler pass...
            You never know if someone is friendly or not!
                You do not have the strength to fight 
                after that battle with the {monster}!
            Instead you go deeper into the {location}...
            Back home you heard that there was a {monument} 
                that held a clue of the jewels location!
                    If you could just find this, 
            surely you will find what you are looking for...
        You have a crude map you had drawn up back home, 
        you pull it out and see if you could find your way...
                    You slowly step forward as you 
            try to trace your steps from the city...
                    Suddenly!! You step {trap}!! 

                        You are dead!
                            _____
                           /     \  
                          | () () |
                           \  ^  /
                            ||||| 
                            uuuuu
                                                        
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->        
        """)
                replay()
               
            elif choice == "exit":
                print(f"Goodbye {character}!")
                exit()
            else:
                print("Invalid entry, try again!")

    # Code for replay the game
def replay():
        replay = input("""
                        Play again? """).lower()

        if replay == "yes" or replay == "y":
            gameplay()
        if replay == "no" or replay == "n":
            print("""
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->            
      _____                                 ____                        
     / ____|                               / __ \                       
    | |  __    __ _   _ __ ___     ___    | |  | | __   __   ___   _ __ 
    | | |_ |  / _` | | '_ ` _ \   / _ \   | |  | | \ \ / /  / _ \ | '__|
    | |__| | | (_| | | | | | | | |  __/   | |__| |  \ V /  |  __/ | |   
     \_____|  \__,_| |_| |_| |_|  \___|    \____/    \_/    \___| |_|   
                                                                        

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->                                                                     
    """)
        quit()

gameplay()