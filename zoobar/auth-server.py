#!/usr/bin/python

import rpclib
import sys
import auth
from debug import *

class AuthRpcServer(rpclib.RpcServer):
    ## Fill in RPC methods here.
    pass

(_, dummy_zookld_fd, sockpath) = sys.argv

s = AuthRpcServer()
s.run_sockpath_fork(sockpath)
