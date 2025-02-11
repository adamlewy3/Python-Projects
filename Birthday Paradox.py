#Monte Carlo Simulation demonstrating the birthday paradox:
#Given X people in one room, what is the probability that two people will have the same birthday?

#Ask user for #of birthdays
#Generate x amount of birthdays 100000 times.
#For each generated birthday, determine if two people have the same birthday. 
#Compute probability.

import datetime, random

#Birthday generator

def birthdaygen(numofBirthdays): 
    #Will return a list of Birthdays
    birthdays = []
    for i in range(numofBirthdays):
        startofYear=datetime.date(2001,1,1)
        randomnumofdays= datetime.timedelta(random.randint(0,364))
        birthday = startofYear+randomnumofdays
        birthdays.append(birthday)
    return birthdays

#Define a function that will determine whether two birthdays are the same:

def getMatch(birthdays):
    for i in len(birthdays):
        for j in len(birthdays):
            if birthdays[i] == birthdays[j]:
                return birthdays[i]
            else:
                return 'No birthdays match.'
            
    
        