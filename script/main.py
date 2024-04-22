from Transaction import *
from Account import *

agr = datetime.now()
lista = []

for i in range(10):
    lista.append(Transaction('Murilo', '6700,57', agr))

acc = Account(True, 22500.35, lista)

acc.toString()