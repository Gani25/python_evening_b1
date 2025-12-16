import datetime as dt
class football_player:

    def __init__(self, first_name, last_name, birth_year, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_year= birth_year
        self.goals = list()

    
    def calculate_age(self):
        return dt.datetime.now().year - self.birth_year

    def add_goals(self, *goals):
        self.goals.extend(goals)
    
    def total_goals(self):
        return sum(self.goals)
    
    def average_goals(self):
        return self.total_goals()/len(self.goals)


    def __str__(self):
        return f"""
Football Player Info
Name = {self.first_name} {self.last_name},
Gender = {self.gender},
Birth Year = {self.birth_year},
Age = {self.calculate_age()},
Goals = {self.goals}
Total Goals = {self.total_goals()},
Average Goals = {self.average_goals()}
"""