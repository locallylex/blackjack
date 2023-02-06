# Catch 100

## Game Objective: 
# Pull the slot machine lever and try to get exactly 100 points. 
# Points randomly incrase by a value of 1-10. If you go over 100 points you lose.

## Project Objective: to become familiar with utilizing while loops; will use this code to build a more complex game of blackjack

import random
game_over = False
score = 0

while not game_over:
    score+= random.randint(1,11)

    print(score)
    
    if score < 99: 
        print("Game is still on!")
    
    if score > 90 and score < 100:
        print("You are getting close to winning...")
        
    if score == 100:
        print("You Win!!")
        break
    
    if score > 100:
        game_over = True
        print("Sorry. You Loose :(")
        break