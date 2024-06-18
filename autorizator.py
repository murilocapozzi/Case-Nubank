from datetime import datetime

def autorizator(transacao, conta):

    result = []

    validate_account_not_active(result, conta)
    validate_first_transaction_above_threshold(result, conta)
    validate_insufficient_limit(result, transacao, conta)
    validate_highfrequency_small_interval(result, transacao, conta)
    validate_doubled_transaction(result, transacao, conta)

    if len(result) == 0:
        print('Transação autorizada')
        conta.addHistory(transacao)
    else:
        print(f'Transação não autorizada pelo(s) motivo(s):')
        for violacao in result:
            print(f'\t{violacao}')


def validate_account_not_active(result, conta):
    
    if conta.getActive() == False:
        result.append('validate_account_not_active')


def validate_first_transaction_above_threshold(result, transacao, conta):
    
    history = conta.getHistory()

    if len(history) > 0:
        return

    valor = transacao.getAmount()
    limite = conta.getAvailableLimit()

    if valor > 0.9 * limite:
        result.append('first_transaction_above_threshold')


def validate_insufficient_limit(result, transacao, conta):

    valor = transacao.getAmount()
    limite = conta.getAvailableLimit()

    if valor > limite:
        result.append('insufficient_limit')


def validate_highfrequency_small_interval(result, transacao, conta):
    
    tempo_intervalo_maximo = 120 # Em segundos
    history = conta.getHistory()
    
    if len(history) < 2:
        return

    horario_atual = datetime.now()
    count = 0
    
    for i in range(len(history)-1, -1, -1):
        
        item = history[i]
        
        if (item.getTime() - horario_atual).total_seconds() > tempo_intervalo_maximo:
            return
        
        count += 1
        
        if count == 2:
            result.append('highfrequency_small_interval')
            return

def validate_doubled_transaction(result, transacao, conta):
    
    tempo_intervalo_maximo = 120 # Em segundos
    history = conta.getHistory()
    
    if len(history) == 0:
        return

    merchant_t = transacao.getMerchant()
    valor_t = transacao.getAmount()

    horario_atual = datetime.now()
    count = 0
    
    for i in range(len(history)-1, -1, -1):
        
        item = history[i]
        
        if (item.getTime() - horario_atual).total_seconds() > tempo_intervalo_maximo:
            return
        
        if merchant_t == item.getMerchant() and valor_t == item.getAmount():
            result.append('doubled_transaction')
            return
            
        