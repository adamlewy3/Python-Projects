#Bagel Game
#Number guessing game. 
# "Pico" when guess has a correct digit in the wrong place
#"Fermi" when guess has a correct digit in the correct place
#"bagels" if your guess has no correct digits. You have 10 tries.

import random

NUM_DIGITS = 4
MAX_GUESSES = 20



def getSecretNum():
    secretNum =''
    numbers = [i for i in range(10)]
    random.shuffle(numbers)
    for i in range(NUM_DIGITS):
        secretNum = secretNum+str(numbers[i])
    return secretNum



def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append(' Fermi')
        elif guess[i] in secretNum:
            clues.append(' Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    
    clues.sort
    return ''.join(clues)

def main():
    print(f'''Welcome to Bagels!
          
          I am thinking of a {NUM_DIGITS}-digit number. Here are some clues.
          I will say:
            Pico, if one digit is correct but in the wrong position.
            Fermi, if one difit is correct and in the right position.
            Bagels, if no digit is correct. 

            If the secret number was 238 and your guess was 843, the clues would be Fermi Pico.  
          ''')
    
    #Main game loop:
    while True:
            #This stores the secret number a player needs to guess.
            secretNum = getSecretNum()
            print("I have thought of a number.")
            print(f"You have {MAX_GUESSES} attempts to get it.")

            numGuesses=1
            while numGuesses<=MAX_GUESSES:
                guess = ''
                while len(guess) != NUM_DIGITS or not guess.isdecimal():
                     print('Guess #{}:'.format(numGuesses))
                     guess = input(' >')
                
                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses +=1

                if guess == secretNum:
                    break
                if numGuesses > MAX_GUESSES:
                    print("You have run out of guesses.")
                    print(f"The answer was {secretNum}")

            print("Do you want to play again?")
            if not input('>').lower().startswith('y'):
                break

            print('Thanks for playing!')
    
            






if __name__ == '__main__':
    main()
