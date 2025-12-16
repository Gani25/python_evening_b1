import cricket_player_module as cpm

virat = cpm.cricket_player("Virat","Kohli",1987,"Male")

virat.add_runs(60,100,0,50,150)

chris = cpm.cricket_player("Chris","Gayle",1980,"Male")
chris.add_runs(20,100,50,60,90)

print(virat)
print(chris)