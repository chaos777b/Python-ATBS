#! /usr/bin/env python3
'''
    File name: randomQuizGenerator.py
    Author: ********************
    Date created: 5/19/2016
    Date last modified: 5/19/2016
    Python Version: 3.5.0
'''
import random, os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 
    'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 
    'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 
    'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 
    'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 
    'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts'
    :'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi'
    :'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska'
    :'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 
    'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 
    'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 
    'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania'
    :'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 
    'South Dakota':'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 
    'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond',
    'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 
    'Madison', 'Wyoming': 'Cheyenne'} 

def genQuiz():
    for quizNum in range(35):
        
        #Creeate quiz and Answer key file.
        quizFile = open('capitalsQuiz%s.txt' % (quizNum +1), 'w')
        answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
        
        #Write out header files for the quiz 
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' 
            % (quizNum + 1)) 
        quizFile.write('\n\n')
    quizFile.close()
    answerKeyFile.close()

def shuffleState():
    states = list(capitals.keys())
    random.shuffle(states)
    return(states)

def writeQuiz(ranStates, questionNum, answerOptions, correctAnswer):
    
    for quizNum in range(35):

        quiz= open('capitalsQuiz%s.txt' % (quizNum +1), 'a')
        answer= open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'a')

        quiz.write('%s. what is the Capital of %s?\n\n' %(questionNum +1,
            ranStates[questionNum]))
        for i in range(4):
            quiz.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quiz.write('\n')

        answer.write('%s. %s\n' % (questionNum +1, 'ABCD'
        [answerOptions.index(correctAnswer)]))
    quiz.close()
    answer.close()

def answerOpts(states):

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wronganswer = list(capitals.values())
        del wronganswer[wronganswer.index(correctAnswer)]
        wronganswer = random.sample(wronganswer, 3)
        answerOptions = wronganswer + [correctAnswer]
        random.shuffle(answerOptions)
        writeQuiz(states, questionNum, answerOptions, correctAnswer)


def main():
    genQuiz()
    randomStates=shuffleState()
    answerOpts(randomStates)


if __name__ == '__main__':
    main()