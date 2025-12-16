import player_module as pm

rohit = pm.cricket_player("Rohit","Sharma",1982,"Male")

rohit.add_runs(100,150,20,0,60)

messi = pm.football_player("Lionel","Messi",1983,"Male")
messi.add_goals(2,5,3,0,1)

print(rohit)
print(messi)