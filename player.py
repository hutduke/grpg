class character():
    max_hp
    current_hp
    max_mp
    current_mp
    max_stats
    current_stats
    exp
    skills

class player(character):
    def __init__(self, name, job):
        self.max_hp = job.hp
        self.max_mp = job.mp
        self.current_hp = self.max_hp
        self.current_mp = self.current_hp
        for stat in self.max_stats:
            stat = 10
        self.current_stats = self.max_stats
        self.job = job
        self.skills = job.skills
        self.exp = 0

class enemy(character):
    def __init__(self, name, race):
        #open enemy file and read it to pull the race values
        self.max_hp = RACE.hp
        self.current_hp = self.max_hp
        self.max_mp = RACE.mp
        self.current_mp = self.max_mp
        self.exp = RACE.exp
        self.skills = RACE.skills
        self.max_stats = RACE.stats
        self.current_stats = self.max_stats

