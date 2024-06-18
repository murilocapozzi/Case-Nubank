import pytest
from account import *
from transaction import *
from autorizator import *
from datetime import datetime, timedelta


def test_valid_validate_account_active():

    result = []
    conta = Account(True, 0, [])
    validate_account_not_active(result, conta)
    
    assert 'validate_account_not_active' not in result

def test_not_valid_validate_account_not_active():
    
    result = []
    conta = Account(False, 0, [])
    validate_account_not_active(result, conta)
    
    assert 'validate_account_not_active' in result


def test_valid_first_transaction_above_threshold():

    result = []
    data = datetime.now()
    conta = Account(True, 100, [])
    transacao = Transaction('a', 10, data)
    validate_first_transaction_above_threshold(result, transacao, conta)
    
    assert 'first_transaction_above_threshold' not in result

def test_not_valid_first_transaction_above_threshold():

    result = []
    data = datetime.now()
    conta = Account(True, 100, [])
    transacao = Transaction('a', 91, data)
    validate_first_transaction_above_threshold(result, transacao, conta)
    
    assert 'first_transaction_above_threshold' in result


def test_valid_insufficient_limit():

    result = []
    data = datetime.now()
    conta = Account(True, 100, [Transaction('a', 50, data)])
    transacao = Transaction('b', 50, data)
    validate_insufficient_limit(result, transacao, conta)
    
    assert 'insufficient_limit' not in result

def test_not_valid_insufficient_limit():

    result = []
    data = datetime.now()
    conta = Account(True, 100, [Transaction('a', 50, data)])
    transacao = Transaction('b', 150, data)
    validate_insufficient_limit(result, transacao, conta)

    assert 'insufficient_limit' in result


def test_valid_highfrequency_small_interval():
    
    result = []
    data = datetime.now()
    history = [
        Transaction('a', 100, data + timedelta(2)),
        Transaction('b', 200, data + timedelta(1))
    ]

    conta = Account(True, 100, history)
    transacao = Transaction('c', 300, data)

    validate_highfrequency_small_interval(result, transacao, conta)

    assert 'highfrequency_small_interval' not in result

def test_not_valid_highfrequency_small_interval():
    
    result = []
    data = datetime.now()
    history = [
        Transaction('a', 100, data),
        Transaction('b', 200, data)
    ]

    conta = Account(True, 100, history)
    transacao = Transaction('c', 300, data)

    validate_highfrequency_small_interval(result, transacao, conta)

    assert 'highfrequency_small_interval' in result
    
    
    
def test_valid_doubled_transaction():
    
    result = []
    data = datetime.now()
    history = [
        Transaction('a', 100, data + timedelta(1))
    ]

    conta = Account(True, 100, history)
    transacao = Transaction('a', 100, data)

    validate_doubled_transaction(result, transacao, conta)

    assert 'doubled_transaction' not in result

def test_not_valid_doubled_transaction():
    
    result = []
    data = datetime.now()
    history = [
        Transaction('a', 100, data)
    ]

    conta = Account(True, 100, history)
    transacao = Transaction('a', 100, data)

    validate_doubled_transaction(result, transacao, conta)

    assert 'doubled_transaction' in result