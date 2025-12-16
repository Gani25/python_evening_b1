import football_player_module as fpm

messi = fpm.football_player("Lionel","Messi",1991,"Male")

messi.add_goals(5,2,3,0,1)

ronaldo = fpm.football_player("Christiano","Ronaldo",1993,"Male")
ronaldo.add_goals(6,1,0,5,3)

print(messi)
print(ronaldo)