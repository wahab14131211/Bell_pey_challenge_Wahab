# Bell_pey_challenge_Wahab
 This repository is a submission for the Bell PEY challenge uploaded by jbhandari: https://github.com/jbhandari/bell_pey_challenge

 The Game of Pred-war
The game of Pred-war is played between many players over many rounds, with the goal of each player being to collect as many tokens as possible. In a single round of Pred-war, each player is matched up against one other player. The player must choose to either cooperate with their opponent, or betray their opponent. The outcome of each round is as follows:

If both players choose to betray, they will receive x tokens each.
If both players choose to cooperate, they will receive y tokens each.
If one player chooses to cooperate while the other player chooses to betray, then the cooperator will receive no tokens, while the betrayer will receive z tokens.
x, y, and z are integers between 1 and 10. In each round it is guaranteed that x < y < z.

Your task
Your task is to write a simple program which will be entered into a game of Pred-war along with all of the other programs written by the other candidates. In each round, your program will be matched against another candidate's program at random. After 10000 rounds, the player with the greatest number of tokens is declared the winner.

Your program will be judged not only on its performance in the game, but also on the originality and thought behind the strategies used. Keep in mind that sometimes the simplest strategies are the best!

Requirements
You may use Python, Ruby, or Java to write your program.
Your program should be implemented as a pure function that will be called once for every round played. For simplicity, your program will have no memory of the results of previous rounds.
The function should take five inputs (x, y, z, r, b), where
x, y, and z are the token rewards for that round, as described above;
r is the round number (between 1 and 10000); and
b is the percentage of time, as a float between 0 and 1, that your opponent for that round has elected to betray their opponent in all of the previous rounds that they have played. For the first round, b will be given as 0.
The function should return the string cooperate or betray.
Include a short description of the reasoning behind your strategy in the comments of your program.
Examples
There are many strategies that you might consider using. Remember that, in each round, you have access to the token reward structure (x, y, z), the degree of progress through the game (r), and a measure of the trustworthiness of your oponent (b). As an example, your program might choose to cooperate with every player for the first half of the game, before betraying every player in the second half. In this case, your submission might look like this in Python:

def my_player(x, y, z, r, b):
    # cooperate with everyone for the first half of the game to gain trust,
    # and then betray everyone to try to gain as many tokens as possible
    if r < 5000:
        return "cooperate"
    return "betray"

