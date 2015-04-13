from debug import *
from zoodb import *
import rpclib

def connect():
    sockname = "/banksvc/sock"
    c = rpclib.client_connect(sockname)
    return c

def setup(username):
    kwargs = {}
    kwargs['username'] = username
    c = connect()
    return c.call('setup',**kwargs)

def transfer(sender, recipient, zoobars, token):
    kwargs = {}
    kwargs['sender'] = sender
    kwargs['recipient'] = recipient
    kwargs['zoobars'] = zoobars
    kwargs['token'] = token
    c = connect()
    return c.call('transfer', **kwargs)

def balance(username):
    kwargs = {}
    kwargs['username'] = username
    c = connect()
    return c.call('balance', **kwargs)

def get_log(username):
    kwargs = {}
    kwargs['username'] = username
    c = connect()
    return c.call('get_log',**kwargs)
