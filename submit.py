#!/usr/bin/python
import os
import sys
import base64
import json
import urllib,urllib2

TOKEN_FILE = 'submit.token'
SUBMIT_URL = 'https://6858submit.csail.mit.edu/capi/submit'

def submit(filename):

    if not os.path.exists(TOKEN_FILE):
        print "Please get a valid token from the submission website and enter it here"
        token = raw_input("token: ").strip()
        with open(TOKEN_FILE,'w') as f:
            f.write(token);

    with open(TOKEN_FILE) as f:
        token = f.read()

    doc = prepare_data(filename,token)

    print "using token: {0}".format(token)

    try:
        urllib2.urlopen(SUBMIT_URL,json.dumps(doc))
        print 'File {0} submitted'.format(filename)
        print 'please visit the submission website to verify your submission.'
    except urllib2.HTTPError as e:
        print "Error submitting file: {0}".format(e)
        print "Maybe your API token has changed or the file is not a tarball?"
        print "Please delete the file 'submit.token' and try again."



def prepare_data(filename,token):

    with open(filename) as f:
        filedata = f.read()

    doc = {
        'filename':filename,
        'api-token':token,
        'data': base64.b64encode(filedata),
    }

    return doc


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage {0} labx-handin.tar.gz".format(sys.argv[0])
        sys.exit(1)
    submit(sys.argv[1])
