from art import castle

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
