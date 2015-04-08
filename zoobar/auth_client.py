from debug import *
from zoodb import *
import rpclib

sockname = "/authsvc/sock"
c = rpclib.client_connect(sockname);

def login(username, password):
    ## Fill in code here.
    kwargs = {}
    kwargs['username'] = username
    kwargs['password'] = password
    return c.call('login', **kwargs)

def register(username, password):
    ## Fill in code here.
    kwargs = {}
    kwargs['username'] = username
    kwargs['password'] = password
    return c.call('register',**kwargs)

def check_token(username, token):
    ## Fill in code here.
    kwargs = {}
    kwargs['username'] = username
    kwargs['token'] = token
    return c.call('check_token',**kwargs)
