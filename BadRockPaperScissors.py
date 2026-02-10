
import random


def f1():
  print("Choose Rock, Paper, or Scissors: ")
  v1 = input()

def f2():
  v3 = random.randrange(1, 4, 1)
  if v3 == 1:
    v4 = "Rock"
  elif v3 == 2:
    v4 = "Paper"
  else:
    v4 = "Scissors"

def f3():
    if v1 == v4:
        print("It's a tie!")
    elif v1 == "Rock" and v4 == "Scissors":
        print("You win!")
    elif v1 == "Paper" and v4 == "Rock":
        print("You win!")
    elif v1 == "Scissors" and v4 == "Paper":
        print("You win!")
    else:
        print("You lose!")