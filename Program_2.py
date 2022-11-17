from random import randint

def CandiesInTheHand(name):
    candies = int(input(f"{name}, how much candies you will take (from 1 to 28): "))
    while candies < 1 or candies > 28:
        candies = int(input(f"{name}, choose only from 1 to 28: "))
    return candies

def Promt(name, k, counter, value):
    print(f"Game: {name} took {k} candies, now {name} has got {counter} candies. {value} candies left on the table.")

player1 = input("Player 1. Enter a name: ")
player2 = input("Player 2. Enter a name: ")
candiesLeft = int(input("How many candies are in the game: "))
flag = randint(0,2)
if flag:
    print(f"The first move {player1}")
else:
    print(f"The first move {player2}")

firstPlayerCandies = 0 
secondPlayerCandies = 0

while candiesLeft > 28:
    if flag:
        candies = CandiesInTheHand(player1)
        firstPlayerCandies += candies
        candiesLeft -= candies
        flag = False
        Promt(player1, candies, firstPlayerCandies, candiesLeft)
    else:
        candies = CandiesInTheHand(player2)
        secondPlayerCandies += candies
        candiesLeft -= candies
        flag = True
        Promt(player2, candies, secondPlayerCandies, candiesLeft)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")