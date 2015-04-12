#!/usr/bin/python
#
# Insert bank server code here.

import rpclib
import sys
import bank
from debug import *
from sqlalchemy.orm import class_mapper

def serialize(model):
    cols = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c,getattr(model,c)) for c in cols)

class BankRpcServer(rpclib.RpcServer):
    def rpc_setup(self, username):
        bank.setup(username)

    def rpc_transfer(self, sender, recipient, zoobars):
        return bank.transfer(sender, recipient, zoobars)

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        #return bank.get_log(username)
        serialized_log = [serialize(log) for log in bank.get_log(username)]
        return serialized_log

(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
