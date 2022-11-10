print("Guess the Number!\n\nYou have to guess a number between 0 and a million and the game will tell you if you have guessed it correctly or not\nTotally Random One-Million-to-One")

import random

attempt = 1
number = random.randint(1,1000000)
while True:
  
  ask = int(input("Your turn to guess the number this game has chosen: "))
  
  if ask<number:
    print("Too low! Guess a bit higher")
    attempt+=1
  elif ask>number:
    print("Too high! Guess a bit lower")
    attempt+=1
  elif ask == number:
    print("Correct! You guessed it")
    
  else:
    print("I'm done with you! You just selected anything other than between 0 and a million?")
    attempt+=1
    exit()
  
  if ask!=number:
    continue
  else:
    print("You guessed the number,",ask,"in attempts: ",attempt)
    break
   

print("You won!")

  
  
