# You should write all four classes in this file
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, x):
        self.age = x
        
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
    def change_grade(self, x):
        self.grade = x
        return self
        
class Staff(Person):
    def __init__(self,name,age,position):
        super().__init__(name,age)
        self.position = position
        
    def get_position(self):
        return self.position
    
    def change_position(self, newPosition):
        self.position = newPosition
        return self
        
class Roster:
    def __init__(self):
        self.roster = []
        
    def add(self, Person):
        self.roster.append(Person)
        
    def size(self):
        return len(self.roster)
        
    def remove(self, Person):
        self.roster.remove(Person)
        
    def get_person(self, name):
        for p in self.roster:
            if p.get_name() == name:
                return p
            
        #if there is no one with that name:
        return None
        
    def map(self, func):
        for p in self.roster:
            func(p)