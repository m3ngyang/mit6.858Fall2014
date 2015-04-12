from debug import *
from zoodb import *
import rpclib

sockname = "/banksvc/sock"
c = rpclib.client_connect(sockname)

def setup(username):
    kwargs = {}
    kwargs['username'] = username
    return c.call('setup',**kwargs)

def transfer(sender, recipient, zoobars):
    kwargs = {}
    kwargs['sender'] = sender
    kwargs['recipient'] = recipient
    kwargs['zoobars'] = zoobars
    return c.call('transfer', **kwargs)

def balance(username):
    kwargs = {}
    kwargs['username'] = username
    return c.call('balance', **kwargs)

def get_log(username):
    kwargs = {}
    kwargs['username'] = username
    return c.call('get_log',**kwargs)
