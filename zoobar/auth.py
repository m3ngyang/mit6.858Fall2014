from zoodb import *
from debug import *

import hashlib
import random

#def newtoken(db, person):
#    hashinput = "%s%.10f" % (person.password, random.random())
#    person.token = hashlib.md5(hashinput).hexdigest()
#    db.commit()
#    return person.token

# Exercise 5
def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return cred.token

def login(username, password):
#    db = person_setup()
#    person = db.query(Person).get(username)
#    if not person:
#        return None
#    if person.password == password:
#        return newtoken(db, person)
#    else:
#        return None
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if not cred:
        return None
    if cred.password == password:
        return newtoken(db,cred)
    else:
        return None

def register(username, password):
#    db = person_setup()
#   person = db.query(Person).get(username)
#    if person:
#        return None
#    newperson = Person()
#    newperson.username = username
#    newperson.password = password
#    db.add(newperson)
#    db.commit()
#    return newtoken(db, newperson)
    persondb = person_setup()
    creddb = cred_setup()
    person = persondb.query(Person).get(username)
    if person:
        return None
    newperson = Person()
    newcred = Cred()
    newperson.username = username
    newcred.username = username
    newcred.password = password
    persondb.add(newperson)
    creddb.add(newcred)
    persondb.commit()
    creddb.commit()
    return newtoken(creddb, newcred)

def check_token(username, token):
#    db = person_setup()
#    person = db.query(Person).get(username)
#    if person and person.token == token:
#        return True
#    else:
#        return False
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False
