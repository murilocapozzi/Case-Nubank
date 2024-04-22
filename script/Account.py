from Transaction import *

class Account:
    def __init__(self, active, availableLimit, history):
        self.active = active
        self.availableLimit = availableLimit 
        self.history = history # Lista de Transaction()

    def getActive(self):
        return self.active
    
    def setActive(self, newActive):
        self.active = newActive

    def getAvailableLimit(self):
        return self.availableLimit
    
    #def setAvailableLimit(self, newAvailableLimit):
    #    self.amount = newAvailableLimit

    def getHistory(self):
        return self.history
    
    def setHistory(self, newHistory):
        self.history = newHistory

    def toString(self):
        print(f'{"Ativa" if self.active == 1 else "Não ativa"}: ${self.availableLimit:.2f} = [')
        for item in self.history:
            acc = item.toString()
            print(f"\t{acc}")
        print(']')