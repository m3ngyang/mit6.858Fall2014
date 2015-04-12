from zoodb import *
from debug import *
import pdb

import time

def transfer(sender, recipient, zoobars):
    #persondb = person_setup()
    #senderp = persondb.query(Person).get(sender)
    #recipientp = persondb.query(Person).get(recipient)
    bankdb = bank_setup()
    sender_bank = bankdb.query(Bank).get(sender)
    recipient_bank = bankdb.query(Bank).get(recipient)

    sender_balance = sender_bank.zoobars - zoobars
    recipient_balance = recipient_bank.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    sender_bank.zoobars = sender_balance
    recipient_bank.zoobars = recipient_balance
    #persondb.commit()
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    #db = person_setup()
    #person = db.query(Person).get(username)
    #return person.zoobars
    #pdb.set_trace()
    db = bank_setup()
    bank = db.query(Bank).get(username)
    return bank.zoobars

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))

def setup(username):
    bankdb = bank_setup()
    newbank = Bank()
    newbank.username = username
    bankdb.add(newbank)
    bankdb.commit()
