joblist = ["Warrior", "Mage", "Rogue", "Cleric"]

class job:
    def __init__(name):
        lookup job info in file
    stat_growth = tuple() #set of numbers (S/D/C/I/W/C)
    equipment = {} #t/f keys for different equipment types
    skills = {} #skill list and associated level requirements
    description = "" #duh

class skill:
    cost = tuple() #set of numbers (HP/MP)
    targets = "" #self/enemy/# of enemies
    effect_type = "" #battle effect/social effect/field effect
    description = "" #duh
    function = "" #for each skill


