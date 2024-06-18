import datetime

class Transaction:
    def __init__(self, merchant, amount, time):
        self._merchant = merchant
        self._amount = amount
        self._time = time

    def getMerchant(self):
        return self._merchant

    def setMerchant(self, newMerchant):
        self._merchant = newMerchant

    def getAmount(self):
        return self._amount

    def setAmount(self, newAmount):
        self._amount = newAmount

    def getTime(self):
        return self._time

    def setTime(self, newTime):
        self._time = newTime

    def __str__(self):
        time = self._time.strftime("%d/%m/%Y %H:%M:%S")
        return (f'({time}) {self._merchant}: ${self._amount}')