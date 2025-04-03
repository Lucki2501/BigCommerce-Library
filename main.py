import init
import bc
import b2b
from time import time, sleep
from utils import pr, file, sheet, UUID, clear
from requests import get, delete
from json import loads


# AUTHENTICATION

bc.auth = {
    'hash': init.hash,
    'token': init.token,
    'other': 'None'
}
init.check() # DO NOT REMOVE

# PLAYGROUND
bc.v2_check(8,True)


# Common samples

# Storefront token
# pr(bc.Token.gql(channel_ids=[1],allowed_cors_origins=['https://plat4m-test.mybigcommerce.com'],expires_at=int(time()+10000)))
# Impersonation token
# pr(bc.Token.customer(channel_id=1,expires_at=int(time()+1000)))

# GraphQL
#pr(bc.gql({
#     'query':'''
#
 #    ''',
  #   'variables':{
#
 #    }
 #},
# token='',
# admin=True,
  #  channel_id=1
#))


