import requests

#=========================================================================#
#                             API REST FETCH                              #
#=========================================================================#

BASE_URI = "https://api.open5e.com/v1/"


################## F1 - Classes #################

def fetch_all_classes()->list[str]:
    '''Fetches all classes names from https://api.open5e.com API.
    
    ENDPOINT: https://api.open5e.com/v1/classes/
    
    Retrieves a list[str] dataset.'''
    CL_URI = BASE_URI + 'classes/'
    response = requests.get(CL_URI)
    if response.status_code == 200:
        dataset = response.json()
        classes = []
        for data in dataset['results']:
            classes.append(data['name'])
        return classes
    else:
        return ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

def fetch_all_backgrounds()->list[str]:
    '''Fetches all background names from https://api.open5e.com API.
    
    ENDPOINT: https://api.open5e.com/v1/backgrounds/
    
    Retrieves a list[str] dataset.'''
    BG_URI = BASE_URI + 'backgrounds/'
    response = requests.get(BG_URI)
    if response.status_code == 200:
        dataset = response.json()
        backgrounds = []
        for data in dataset['results']:
            backgrounds.append(data['name'])
        return backgrounds
    else:
        return ['Acolyte', 'Artisan', 'Charlatan', 'Con Artist', 'Court Servant', 'Crime Syndicate Member', 'Criminal', 'Desert Runner', 'Destined', 'Diplomat', 'Elemental Warden', 'Entertainer', 'Exile', 'Farmer', 'Fate-Touched', 'Folk Hero', 'Forest Dweller', 'Former Adventurer', 'Freebooter', 'Gambler', 'Gamekeeper', 'Guildmember', 'Hermit', 'Innkeeper', 'Lyceum Student', 'Marauder', 'Mercenary Company Scion', 'Mercenary Recruit', 'Monstrous Adoptee', 'Mysterious Origins', 'Northern Minstrel', 'Occultist', 'Outlander', 'Parfumier', 'Recovered Cultist', 'Sage', 'Sailor', 'Scoundrel', 'Sentry', 'Trader', 'Trophy Hunter', 'Urchin']

def retrieve_all_alignments()->list[str]:
    '''Retrieves all alignments.
    
    Retrieves a list[str] dataset.'''
   
    return ["lawful good", "neutral good", "chaotic good", "lawful neutral", "true neutral", "chaotic neutral", "lawful evil", "neutral evil", "chaotic evil"]

def fetch_all_races()->list[str]:
    '''Fetches all background names from https://api.open5e.com API.
    
    ENDPOINT: https://api.open5e.com/v1/races/
    
    Retrieves a list[str] dataset.'''
    RC_URI = BASE_URI + 'races/'
    response = requests.get(RC_URI)
    if response.status_code == 200:
        dataset = response.json()
        races = []
        for data in dataset['results']:
            races.append(data['name'])
        print(races)
        return races
    else:
        return ['Alseid', 'Catfolk', 'Darakhul', 'Derro', 'Dragonborn', 'Drow', 'Dwarf', 'Elf', 'Erina', 'Gearforged', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Minotaur', 'Mushroomfolk', 'Satarre', 'Shade', 'Tiefling']


# if __name__ == '__main__':
#     fetch_all_classes()
#     fetch_all_backgrounds()
#     fetch_all_races()