#!/usr/bin/python3 -tt
#Automate the borning stuff UDEMY class Guesss the numbe game

import random, sys, re

def inCheckName(preName):

	for maxTries in range(5):
		if not preName:
			print("You did not enter a valid name, please entere your name: ", end ="")
			preName = input()
		if preName.isdigit() == True:
			print("You did not enter a valid name, please entere your name: ", end ="")
			preName = input()
		if re.search("[0-9]+", preName):
			print("You did not enter a valid name, please entere your name: ", end ="")
			preName = input()

	if maxTries == 4 and not preName or re.search("[0-9]+", preName):
		print("You tried to many times, exiting the program!")
		sys.exit()

	return( preName)




print('Hello. What is your name?: ', end ="")


pstName = inCheckName(input())


intSecretNumber = random.randint(1,20)
print('Well ' + pstName + " I'm thining of a number between 1 and 20.")

#Ask the play to guess 6 times.

for intguesTaken in range(1,7):
	print(pstName +' please take a guess:', end ="")
	intguess = int(input())

	if intguess < intSecretNumber:
		print(pstName + ' your guess is two low.')
	elif intguess > intSecretNumber:
		print(pstName +' your Guess is to high.')
	else:
		break
if intguess ==intSecretNumber:
	print('Good Job! ' +pstName + ' you guessed my number in ' + str(intguesTaken) + ' guesses!')
else:
	print('Nope. the number I was thinking of was '+ str(intSecretNumber))