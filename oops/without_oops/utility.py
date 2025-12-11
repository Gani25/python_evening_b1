# All the functions with respect to players

import datetime as dt

def add_scores(*scores, player):

    player["runs"].extend(scores)

def calculate_age(player):
    player["age"] = dt.datetime.now().year - player["birth_year"]


def total_and_avg_runs(player):

    total_runs = sum(player["runs"])
    avg_runs = total_runs / len(player["runs"])
    return total_runs, avg_runs

def display_player(player):
    total_runs,avegrage_runs = total_and_avg_runs(player)
    calculate_age(player)
    print("-----------------------------------------------------")
    print("Player Information")
    print(f"Name = {player["name"]}")
    print(f"Gender = {player["gender"]}")
    print(f"Birth Year = {player["birth_year"]}")
    print(f"Age = {player["age"]}")
    print(f"Runs = {player["runs"]}")
    print(f"Total Runs = {total_runs}")
    print(f"Average Runs = {avegrage_runs}")
    print("-----------------------------------------------------")