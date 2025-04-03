import secrets
import bc
import sys

msf_hash = secrets.msf_hash
msf_token = secrets.msf_token

v2_hash = secrets.v2_hash
v2_token = secrets.v2_token

code_hash = secrets.code_hash
code_token = secrets.code_token

hash = secrets.hash
token = secrets.token

other = secrets.other

b2b_token = secrets.b2b

def check():
    if bc.auth['token']==token:
        prompt = input(f'You are using a merchant Token for {secrets.hash}, please confirm with enter ')
        if prompt == '':
            return
        else:
            print('Ending program')
            sys.exit()
            
# b2b path = https://api.bundleb2b.net/api/v3/io/


