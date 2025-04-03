import secrets
import bc


test_hash = secrets.test_hash
test_token = secrets.test_token

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


