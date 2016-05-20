#!/usr/bin/python3 -tt
#Automate the borning stuff UDEMY class
print('How many cats do you have?')
numCats = input()
try:
	if int(numCats) >= 4:
		print('That is a lot of cats')
	else:
		print('That is not that many cats.')
except ValueError:
	print('You did not enter a number.')