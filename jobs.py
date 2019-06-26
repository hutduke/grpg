joblist = ["Warrior", "Mage", "Rogue", "Cleric"]

class job:
    def __init__(self, name):
        #lookup job info in file
        jobsfile = open("jobs", "r")
        #split on commas!?!?!?!
        #otherwise use a JSON style format?
        self.hp = 10 #different starting values for each job
        self.mp = 10 #different starting values for each job
        self.stat_growth = tuple() #set of numbers (S/D/C/I/W/C)
        self.equipment = {} #t/f keys for different equipment types
        self.skills = {} #skill list and associated level requirements
        self.description = "" #duh

class skill:
    def __init__(self, job):
        #lookup info in skills file
        self.cost = tuple() #set of numbers (HP/MP)
        self.targets = "" #self/enemy/# of enemies
        self.effect_type = "" #battle effect/social effect/field effect
        self.name
        self.description = "" #duh
        self.function = "" #for each skill
