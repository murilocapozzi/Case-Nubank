from datetime import datetime

class Transaction:
    def __init__(self, merchant, amount, time):
        self.merchant = merchant
        self.amount = amount
        self.time = time

    def getMerchant(self):
        return self.merchant
    
    def setMerchant(self, newMerchant):
        self.merchant = newMerchant

    def getAmount(self):
        return self.amount
    
    #def setAmount(self, newAmount):
    #    self.amount = newAmount

    def getTime(self):
        return self.time
    
    def setTime(self, newTime):
        self.time = newTime

    def toString(self):
        time = self.time.strftime("%d/%m/%Y %H:%M:%S")
        return (f'({time}) {self.merchant}: ${self.amount}')