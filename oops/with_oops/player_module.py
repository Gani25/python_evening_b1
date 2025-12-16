import datetime as dt
class player:

    def __init__(self, first_name, last_name, birth_year, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_year= birth_year

    
    def calculate_age(self):
        return dt.datetime.now().year - self.birth_year

   

    def __str__(self):
        return f"""
Player Info
Name = {self.first_name} {self.last_name},
Gender = {self.gender},
Birth Year = {self.birth_year},
Age = {self.calculate_age()}
"""
    
# Inheritance: 
class cricket_player (player):

    def __init__(self, first_name, last_name, birth_year, gender):
        super().__init__(first_name, last_name, birth_year, gender)
        self.runs = list()
    
    def add_runs(self, *runs):
        self.runs.extend(runs)
    
    def total_runs(self):
        return sum(self.runs)
    
    def average_runs(self):
        return self.total_runs()/len(self.runs)


    def __str__(self):
        return f"""
{super().__str__()}
Cricket Player Info
Runs = {self.runs}
Total Runs = {self.total_runs()},
Average Runs = {self.average_runs()}
"""

class football_player (player):

    def __init__(self, first_name, last_name, birth_year, gender):
        super().__init__(first_name, last_name, birth_year, gender)
        self.goals = list()

    def add_goals(self, *goals):
        self.goals.extend(goals)
    
    def total_goals(self):
        return sum(self.goals)
    
    def average_goals(self):
        return self.total_goals()/len(self.goals)


    def __str__(self):
        return f"""
{super().__str__()}
Football Player Info
Goals = {self.goals}
Total Goals = {self.total_goals()},
Average Goals = {self.average_goals()}
"""