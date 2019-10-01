#mathew hobson
import random
pScore = 0
cScore = 0
ties = 0

cMoves = ["r", "p", "s"]

def printscore():
	print("Score: ")
	print(pname + ":" + str(pScore))
	print("Computer score:" + str(cScore))
	print("Ties: " + str(cScore))


print("Welcome to rock paper scissors")
pname = input("What is your name? ")

while True:
	pMove = input("What is your move?:'r' rock, 'p' paper, 's' scissors, or quit 'q' ")

	printscore()

	if pMove == 'q':
		break
	cMove = random.choice(cMoves)

	if pMove == "r":
		print(pname + "picked rock")
		if cMoves == "r": 
			print("Computer picks rock")
			print("tie")
			ties += 1
		elif cMove == "p"
			print("Computer pick Paper")
			print("Paper covers rock")
			cScore += 1
		else:
			print("Computer picked scissors")
			print("rock breaks scissors")
			pScore += 1
	elif pMove == "p"
		pass

	elif pMove == "s"

	else:
		print("not an option")

