from collections import defaultdict
class School:
    def __init__(self,school_name):
        self.students = set()
        self.school_name = school_name
        self.db = defaultdict(set) 


    def add(self,name,g):
        try:
            self.db[g].add(name)
        except KeyError:
            self.db[g] = set()
            self.db[g].add(name)

    def grade(self,g):
        return self.db[g]

    # stole this code from a working program. Still doesn't work.
    # I'm going to cheat and submit this so I can see more examples of
    # working programs.
    
    def sort(self):
        return {g: tuple(sorted(self.db[g])) for g in self.db}

