from art import cross

def battle(monster, character, early_death, journey_time):
    '''monster battle'''
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

def monster_loss(monster, location):
    '''scenario where monster dies'''
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