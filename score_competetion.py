def manage_scoreboard():
    for player_number, player_score in my_list:
        if f"player {player_number}" not in score:
            score[f"player {player_number}"] = player_score
        else:
            score[f"player {player_number}"] += player_score
    return score
    

my_list=[]
n=int(input("Enter number of rounds: "))
score={
    
}
if n<1:
    print("ERROORR: enter more players")
else:
    for i in range(n):
        z=tuple(eval(input("Enter player number and his score: ")))
        my_list.append(z)
print (manage_scoreboard())