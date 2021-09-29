#execution 1
rounds=input("How many rounds do you want to play? ")
attempts=0
for i in range(int(rounds)):
  num=7
  guess=input("Guess a number from 1-10: ")
  if int(guess) >=1:
    each=1
  if int(num)==int(guess):
    print("You got it!")
  if int(guess)>int(num):
    print("Too high!")
  elif int(guess)<int(num):
    print("Too low!")
  attempts=attempts+each
print("Attempts = "+str(attempts))

#execution 2, random and avg score

"""rounds=input("How many rounds do you want to play? ")
attempts=0
score=0
import random
num=random.randint(1,10)
for i in range(int(rounds)):
  guess=input("Guess a number from 1-10: ")
  if int(guess) >=1:
    each=1
  if int(num)==int(guess):
    points=1
    print("You got it!")
  if int(guess)>int(num):
    points=0
    print("Too high!")
  elif int(guess)<int(num):
    points=0
    print("Too low!")
  attempts=attempts+each
  score=score+points
print("Attempts = "+str(attempts), "Score = "+str(score))


#execution 3, timed
rounds=input("How many rounds do you want to play? ")
attempts=0
score=0
import random
num=random.randint(1,10)
import time
for i in range(int(rounds)):
  start=time.time()
  print("Start")
  guess=input("Guess a number from 1-10: ")
  if int(guess) >=1:
    each=1
  if int(num)==int(guess):
    points=1
    print("You got it!")
    end=time.time()
  if int(guess)>int(num):
    points=0
    print("Too high!")
    end=time.time()
  elif int(guess)<int(num):
    points=0
    print("Too low!")
    end=time.time()
  attempts=attempts+each
  score=score+points
  time=end-start
print("Attempts = "+str(attempts)+", "+"Score = "+str(score)+", "+"Time = "+str(round(time))+" sec.")
"""
