import os

def DrawAField(inputMoves):
	os.system('cls')
	print("*" * 3, "prompt", "*" * 3)
	print("-" * 13)
	for i in range(3):
		print(f"| {1 + i * 3} | {2 + i * 3} | {3 + i * 3} |")
		print("-" * 13)
	print()
	print("*", "game field", "*")
	print("-" * 13)
	for i in range(3):
		print(f"| {inputMoves[0 + i * 3]} | {inputMoves[1 + i * 3]} | {inputMoves[2 + i * 3]} |")
		print("-" * 13)

def CheckWin(playerOne, playerTwo):
	win = 0
	WinCoord = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4 ,7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
	for i in range(len(WinCoord)):
		count = 0
		for j in range(len(WinCoord[i])):
			for k in playerOne:
				if k == WinCoord[i][j]:
					count += 1
				if count == 3:
					return 1	
	for i in range(len(WinCoord)):
		count = 0
		for j in range(len(WinCoord[i])):
			for k in playerTwo:
				if k == WinCoord[i][j]:
					count += 1
				if count == 3:
					return 2

def MakeMove(inputText, moves):
	playerOne = []
	playerTwo = []
	i = 0
	while i != 9:
		try:
			move = int(input(f"{inputText}"))
			print()
			if (move < 1) or (9 < move):
				print("Error. Only numbers from 1 to 9. Try again...")
			else:
				if i % 2 == 0:
					if moves[move - 1] != ' ':
						print("Error. Make another move...")
					else:
						moves[move - 1] = 'X'
						playerOne.append(move - 1)
						i += 1
				else:
					if moves[move - 1] != ' ':
						print("Error. Make another move...")
					else:
						moves[move - 1] = 'O'
						playerTwo.append(move - 1)
						i += 1
		except ValueError:
			print("Error. Only integer numbers. Try again...")
		DrawAField(moves)
		if len(playerOne) >= 3:
			win = CheckWin(playerOne, playerTwo)
			if win == 1:
				i = 9
				print("Player 'X' wins!")
			elif win == 2:
				i = 9
				print("Player 'O' wins!")
			elif (i == 9) and (win == 0):
				print("It's a draw!'")


moves = [' ' for i in range(10)]
DrawAField(moves)	
MakeMove("Enter number from 1 to 9: ", moves)
print("\n")