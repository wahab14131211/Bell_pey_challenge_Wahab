from random import *

#This script is a simple version of the predwar game described in the challenge statement.
#This is used to test 2 strategies, to determine which one is better

def player2(x,y,z,b,r,k):
    #where k is the desired betrayal rate for player2
    if randint(0,100) < k:
        return "cooperate"
    else:
        return "betray"

def wahab_predwar (x,y,z,b,r):

    if (r**1.1)>randint(1,10000):
        avg_tokens_lost= ((x*b) + (z-y)*(1-b))/2
        if avg_tokens_lost <= 1:
            return "cooperate"
        return "betray"

    else:
        if b>0.85 or (b>0.0001 and b<0.15):
            return "betray"
        if (z-y)/(y-x)>= 1:
            return "betray"
        return "cooperate"

player1_tokens=0
player2_tokens=0
player1_betrayals=0
player2_betrayals=0

for round in range (1,10001):
    token = []
    for _ in range (3):
        num = randint(1,10)
        while num in token:
            num = randint(1,10)
        token.append(num)
    token.sort()

    player1_choice=wahab_predwar(token[0],token[1],token[2],player2_betrayals/round,round)
    player2_choice=player2(token[0],token[1],token[2],player1_betrayals/round,round,randint(0,100))

    if (player1_choice == "betray" and player2_choice == "betray"):
        player1_tokens += token[0]
        player2_tokens += token[0]
        player1_betrayals += 1
        player2_betrayals += 1
    elif (player1_choice == "cooperate" and player2_choice == "cooperate"):
        player1_tokens += token[1]
        player2_tokens += token[1]
    else:
        if (player1_choice == "betray"):
            player1_tokens += token[2]
            player1_betrayals += 1
        else:
            player2_tokens += token[2]
            player2_betrayals += 1
print ("Player1:\n\tTokens:%i\n\tBetrayal:%f\nPlayer2\n\tToken:%i\n\tBetrayal:%f"% (player1_tokens,player1_betrayals/10000,player2_tokens,player2_betrayals/10000.0))
