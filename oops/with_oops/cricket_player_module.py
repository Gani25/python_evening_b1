import datetime as dt
class cricket_player:

    def __init__(self, first_name, last_name, birth_year, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_year= birth_year
        self.runs = list()

    
    def calculate_age(self):
        return dt.datetime.now().year - self.birth_year

    def add_runs(self, *runs):
        self.runs.extend(runs)
    
    def total_runs(self):
        return sum(self.runs)
    
    def average_runs(self):
        return self.total_runs()/len(self.runs)


    def __str__(self):
        return f"""
Cricket Player Info
Name = {self.first_name} {self.last_name},
Gender = {self.gender},
Birth Year = {self.birth_year},
Age = {self.calculate_age()},
Runs = {self.runs}
Total Runs = {self.total_runs()},
Average Runs = {self.average_runs()}
"""