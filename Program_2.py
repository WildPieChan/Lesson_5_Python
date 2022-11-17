from random import randint

def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Error. Only integer numbers. Try again...")
    return number

def PlayWithBot():
    ok = False
    while not ok:
        answer = input("Do you want play with bot? Y/N: ")
        if (answer == 'Y') or (answer == 'y') or (answer == 'N') or (answer == 'n'):
            ok = True      
        else:
            print("Error. Use only 'Y' (yes) or 'N' (no) to answer.")
    if (answer == 'Y') or (answer == 'y'):
        print("Choose your enemy:")
        ok = False
        while not ok:
            answer = InputNumber("1: Peter (easy mod).\n2: Sam (hard mod).\n1/2: ")
            if (answer == 1) or (answer == 2):
                ok = True
            else:
                print("Error. Choose only from two players (1 or 2).")
        if (answer == 1):
            return 1
        else:
            return 2
    else:
        return 0

def CandiesInTheHand(name):
    candies = InputNumber(f"{name}, how much candies you will take (from 1 to 28): ")
    while candies < 1 or candies > 28:
        candies = InputNumber(f"{name}, choose only from 1 to 28: ")
    return candies

def EasyBotCandies(name):
    candies = randint(1, 29)
    print(f"{name}, how much candies you will take (from 1 to 28): {candies}")
    return candies

def HardBotCandies(name, candiesOnTheTable):
    if candiesOnTheTable % (28 + 1) != 0:
        candies = candiesOnTheTable % (28 + 1)
    else:
        candies = randint(1, 29)
    print(f"{name}, how much candies you will take (from 1 to 28): {candies}")
    return candies

def Promt(name, k, counter, value):
    print(f"Game: {name} took {k} candies, now {name} has got {counter} candies. {value} candies left on the table.")

gameVsBot = PlayWithBot()
player1 = input("Player 1. Enter a name: ")
if gameVsBot == 1:
    player2 = "Peter"
elif gameVsBot == 2:
    player2 = "Sam"
else:
    player2 = input("Player 2. Enter a name: ")

candiesLeft = InputNumber("How many candies are in the game: ")
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
        if gameVsBot == 1:
            candies = EasyBotCandies(player2)
            secondPlayerCandies += candies
            candiesLeft -= candies
            flag = True
            Promt(player2, candies, secondPlayerCandies, candiesLeft)
        elif gameVsBot == 2:
            candies = HardBotCandies(player2, candiesLeft)
            secondPlayerCandies += candies
            candiesLeft -= candies
            flag = True
            Promt(player2, candies, secondPlayerCandies, candiesLeft)
        else:
            candies = CandiesInTheHand(player2)
            secondPlayerCandies += candies
            candiesLeft -= candies
            flag = True
            Promt(player2, candies, secondPlayerCandies, candiesLeft)

if flag:
    print(f"{player1} wins!")
else:
    print(f"{player2} wins!")