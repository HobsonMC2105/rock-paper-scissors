#mathew hobson
#added comment for github

import random
pScore = 0
cScore = 0
ties = 0

cMoves = ["r", "p", "s"]

def printscore():
	print("Score: ")
	print(pname + ":" + str(pScore))
	print("Computer score:" + str(cScore))
	print("Ties: " + str(ties))


print("Welcome to rock paper scissors")
pname = input("What is your name? ")

while True:
	pMove = input("What is your move?:'r' rock, 'p' paper, 's' scissors, or quit 'q' ")

	if pMove == 'q':
		break
	cMove = random.choice(cMoves)

	if pMove == "r":
		print(pname + " picked rock")
		if cMove == "r": 
			print("Computer picks rock")
			print("tie")
			ties += 1
		elif cMove == "p":
			print("Computer pick Paper")
			print("Paper covers rock")
			cScore += 1
		else:
			print("Computer picked scissors")
			print("rock breaks scissors")
			pScore += 1
	elif pMove == "p":
		print(pname + " picked paper")
		if cMove == "r": 
			print("Computer picks rock")
			print("Paper covers rock")
			pScore += 1
		elif cMove == "p":
			print("Computer pick Paper")
			print("tie")
			ties += 1
		else:
			print("Computer picked scissors")
			print("Scissors cuts paper")
			cScore += 1

	elif pMove == "s":
		print(pname + " picked scissors")
		if cMove == "r": 
			print("Computer picks rock")
			print("Rock breaks scissors")
			cScore += 1
		elif cMove == "p":
			print("Computer pick Paper")
			print("Scissors cuts paper")
			pMove += 1
		else:
			print("Computer picked scissors")
			print("tie")
			ties += 1

	else:
		print("not an option")

	printscore()

