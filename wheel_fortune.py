# WOFPlayer CLASS 
class WOFPlayer():
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self,amt):
        self.prizeMoney += amt    
    def goBankrupt(self):
        self.prizeMoney = 0        
    def addPrize(self, prize):
        self.prizes.append(prize)
    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)
    
# WOFHumanPlayer class definition 
class WOFHumanPlayer(WOFPlayer):
        
    def getMove(self, category, obscuredPhrase, guessed):
        print("""{} has ${}\n Category: {}\n Phrase:  {} \n
        Guessed: {}""".format(self.name, self.prizeMoney, category, obscuredPhrase, guessed))
        return input("Guess a letter, phrase, or type 'exit' or 'pass':")
        
# WOFComputerPlayer class definition 
class WOFComputerPlayer(WOFPlayer):
             
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty 
    def smartCoinFlip(self):
        if (random.randint(1, 10) > self.difficulty):
             return False
        else:
             return True
             
    def getPossibleLetters(self, guessed):
        lst_letters = []
        for LETTER in LETTERS:
             if LETTER not in guessed:
                if LETTER in VOWELS:
                     if self.prizeMoney >= VOWEL_COST:
                        lst_letters.append(LETTER)
                else:         
                     lst_letters.append(LETTER)
        return lst_letters
             
    def getMove(self, category, obscuredPhrase, guessed): 
        r_SORTED_FREQUENCIES_lst = list(self.SORTED_FREQUENCIES)
        r_SORTED_FREQUENCIES_lst.reverse()
        i = 0
        for VOWEL in VOWELS:
             if VOWEL in self.getPossibleLetters(guessed):
                i += 1
        if i == 0:
             return 'pass'
        if self.smartCoinFlip():
            for L in r_SORTED_FREQUENCIES_lst:
                if L in self.getPossibleLetters(guessed):
                     return L
        else:
             return random.choice(self.getPossibleLetters(guessed))
        
import json
import random
import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250

# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))

# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)