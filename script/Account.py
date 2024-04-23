from Transaction import *

class Account:
    def __init__(self, active, availableLimit, history):
        self.__active__ = active
        self.__availableLimit__ = availableLimit 
        self.__history__ = history # Lista de Transaction()

    def getActive(self):
        return self.__active__
    
    def setActive(self, newActive):
        self.__active__ = newActive

    def getAvailableLimit(self):
        return self.__availableLimit__
    
    #def setAvailableLimit(self, newAvailableLimit):
    #    self.amount = newAvailableLimit

    def getHistory(self):
        return self.__history__
    
    def setHistory(self, newHistory):
        self.__history__ = newHistory

    def addHistory(self, item, index=-1):

        if index == -1:
            self.__history__.append(item)
        else:
            if 0 <= index <= len(self.__history__) - 1:
                self.__history__.insert(index, item)
        
    def removeHistory(self, index):

        if 0 <= index <= len(self.__history__) - 1:
            self.__history__.pop(index)

    def toString(self):
        print(f'{"Ativa" if self.__active__ == 1 else "Não ativa"}: ${self.__availableLimit__:.2f} = [')
        for item in self.__history__:
            acc = item.toString()
            print(f"\t{acc}")
        print(']')