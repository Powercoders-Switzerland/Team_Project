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