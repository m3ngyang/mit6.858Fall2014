from debug import *
from zoodb import *
import rpclib

sockname = "/authsvc/sock"

def login(username, password):
    ## Fill in code here.
    kwargs = {}
    kwargs['username'] = username
    kwargs['password'] = password
    c = rpclib.client_connect(sockname);
    return c.call('login', **kwargs)

def register(username, password):
    ## Fill in code here.
    kwargs = {}
    kwargs['username'] = username
    kwargs['password'] = password
    c = rpclib.client_connect(sockname);
    return c.call('register',**kwargs)

def check_token(username, token):
    ## Fill in code here.
    kwargs = {}
    kwargs['username'] = username
    kwargs['token'] = token
    c = rpclib.client_connect(sockname);
    return c.call('check_token',**kwargs)
