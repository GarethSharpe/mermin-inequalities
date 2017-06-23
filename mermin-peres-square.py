'''
created by Gareth Sharpe on June 23, 2017
written by Gareth Sharpe on June 23, 2017

@author: Gareth Sharpe
'''

from random import choice
from pprint import pprint

def classical_magic_square():
    
    # rows start at index = 0
    rows = [0, 1, 2]
    cols = [1, 1, 2]
    
    classical_square = [[1, 1, 1], [1, -1, -1], [-1, +1, '?']]
    
    r = choice(rows)
    c = choice(cols)
    
    print("Row: " + str(r + 1), end=', ')
    print("Col: " + str(c + 1))
    
    alice_choice = classical_square[r]
    bob_choice = []
    i = 0
    for row in classical_square:
        bob_choice.append(classical_square[i][c])
        i += 1
        
    print("Alice's choice: ", end='')
    pprint(alice_choice)
    print("Bob's choice: ", end='  ')
    pprint(bob_choice)
    
    win = 1
    if r == 2 and c == 2:
        win = 0
    
    print("Round outcome: ", win)
    
    return win
    
def classical_square(rounds):
    
    wins = 0
    
    i = 1
    while i <= rounds:
        print("--------------------")
        print("ROUND " + str(i))
        print("--------------------")
        wins += classical_magic_square()
        i += 1
    
    print()
    print("--------------------")
    print("FINAL RESULTS")
    print("--------------------")
    print("Rounds: " + str(rounds))
    print("Wins: ", str(wins))
    print("Losses: " + str(rounds - wins))
    print("Probability of Success: " + str(wins / rounds))

classical_square(10000)
