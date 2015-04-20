from collections import defaultdict
class School:
    def __init__(self,school_name):
        self.students = set()
        self.school_name = school_name
        self.db = {} 


    def add(self,name,grade):
        try:
            self.db[grade].add(name)
        except KeyError:
            self.db[grade] = set()
            self.db[grade] = self.db.[grade].add(name)
            
