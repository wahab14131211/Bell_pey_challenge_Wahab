from random import randint

def wahab_predwar (x,y,z,b,r):
    #The b value becomes more representative of the opponents actions as the rounds progress.
        #Compare the scaled version of r to a random number to determine if the player can be sufficently confident in the accuracy of b

    #if player is confident in the accuracy of b, calculate the risk of cooperating by determining the average number of tokens lost by cooperating
        #The function to calcuate this will return a value from 0.5 to 4. So, if the value is small, cooperate.
    
    #if player is NOT confident in the accuracy of b, check if opponent has a strong tendency to cooperate or betray (ignore this check if game has just started, and b==0)
        #if z-y is larger than y-x, it would be better to betray, otherwise cooperate (since betray heavy players will be filtered out by this point, the player does not need to worry about the exact value of x)

    if (r**1.1)>randint(1,10000):                   #raise r to the power of 1.1 so that by round ~5000, the player is sufficently confident in the validity of b
        avg_tokens_lost= ((x*b) + (z-y)*(1-b))/2    #avg_tokens_lost is average # of tokens lost of player elects to cooperate.
        if avg_tokens_lost <= 1:
            return "cooperate"
        return "betray"

    else:
        if b>0.85 or (b>0.0001 and b<0.15):
            return "betray"
        if (z-y)/(y-x)>= 1:
            return "betray"
        return "cooperate"
