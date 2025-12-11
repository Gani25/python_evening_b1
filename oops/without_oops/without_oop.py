import utility as util

rohit = {
    "name":"Rohit Sharma",
    "gender":"Male",
    "runs":[],
    "birth_year":1984
}

util.add_scores(60,100,45,0, player=rohit)

print(rohit)


chris = {
    "name":"Chris Gayle",
    "gender":"Male",
    "runs":[],
    "birth_year":1980
}

# Add Score
util.add_scores(60,20,45,10, player=chris)


print(chris)

util.display_player(rohit)
util.display_player(chris)