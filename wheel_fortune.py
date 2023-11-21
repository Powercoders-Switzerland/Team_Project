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
         