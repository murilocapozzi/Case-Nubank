from transaction import *

class Account:
    def __init__(self, active, availableLimit, history=[]):
        self._active = active
        self._availableLimit = availableLimit
        self._history = history

    def getActive(self):
        return self._active

    def setActive(self, newActive):
        self._active = newActive

    def getAvailableLimit(self):
        return self._availableLimit

    def setAvailableLimit(self, newAvailableLimit):
        self._amount = newAvailableLimit

    def getHistory(self):
        return self._history

    def setHistory(self, newHistory):
        self._history = newHistory

    def addHistory(self, item, index=-1):

        if index == -1:
            self._history.append(item)
        else:
            if 0 <= index <= len(self._history) - 1:
                self._history.insert(index, item)

    def removeHistory(self, index):

        if 0 <= index <= len(self._history) - 1:
            self._history.pop(index)

    def __str__(self):
        print(f'{"Ativa" if self._active == 1 else "Não ativa"}: ${self._availableLimit:.2f} = [')
        for item in self._history:
            acc = item.toString()
            print(f"\t{acc}")
        print(']')