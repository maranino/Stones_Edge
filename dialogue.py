from art import castle, you_win
import random

def intro(character, inventory, beginning_date):
    '''first intro of the game'''
    print(f"""
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                        Adventurer: {character.name}
                        Weapon: {inventory.weapon}
                        Armor: {inventory.armor}
                        HP: {character.hp}
                        MP: {character.mp}
                        Damage: {character.damage}
                        Magic: {character.magic}
                        Magic Defense: {character.magic_defense}
                        Luck: {character.luck}
        
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

                    The date is {beginning_date.strftime('%B')} {beginning_date.day}, {beginning_date.year}
                        You are named {character.name},
            a {character.job} from the Royal City of Stone's Edge.
      On your free time, you practice sparing with your {inventory.weapon},
                    pretending to be an adventurer. 

    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->
""", castle(), """
        ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->

            There has been a rumor floating around town...    
            of a rare jewel the King lost on his last journey.
                            Problem is...    
            the details seem to change depending on who you ask.
            You have four different options of where to go...    
                        Which will you choose? 

        ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->""")


def traveler_encounter(location, monster):
    '''traveler encounter scenario'''
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

def deny_traveler_encounter(monster, location, trap_death, journey_time):
    '''scenario where you deny the traveler encounter'''
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

                  You have died on {trap_death.strftime('%B')} {trap_death.day}, {trap_death.year}!
                  Your journey lasted {journey_time['journey4']} days.
                                                        
    ->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->        
        """)
    
def traveler_prizes(game_date, journey_time, location, monster):
    '''game of chance with the traveler to get the clue for the jewel'''
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
        


                    """, you_win(), f"""

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

def game_lost(location):
    '''scenario where you lose the game with the traveler'''
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

def traveler_clue(location, end_date, journey_time):
    '''clues that the traveler may give you if you win the game'''
    chance = [f"There are no hints or clues at this {location.monument}!",
              f"The jewel you look for has already been taken by {location.traveler}!"]
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