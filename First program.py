#!/usr/bin/python -tt
#Automate the borning stuff UDEMY class first program

#This program says hello and asks for my name

print ('Hellow World!')
print ('What is your name?') #ask for thier name
strMyName = input()
print('If is good to meet you, ' + strMyName)
print('The length of your name is:')
print(len(strMyName))
print('What is your age?:' end="") #ask for thier age
intMyAge = input()
print('You will be ' + str(int(intMyAge) +1) + ' in a year.')