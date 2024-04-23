import datetime

class Transaction:
    def __init__(self, merchant, amount, time):
        self.__merchant__ = merchant
        self.__amount__ = amount
        self.__time__ = time

    def getMerchant(self):
        return self.__merchant__
    
    def setMerchant(self, newMerchant):
        self.__merchant__ = newMerchant

    def getAmount(self):
        return self.__amount__
    
    #def setAmount(self, newAmount):
    #    self.__amount__ = newAmount

    def getTime(self):
        return self.__time__
    
    def setTime(self, newTime):
        self.__time__ = newTime

    def toString(self):
        time = self.__time__.strftime("%d/%m/%Y %H:%M:%S")
        return (f'({time}) {self.__merchant__}: ${self.__amount__}')