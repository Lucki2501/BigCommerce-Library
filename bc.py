from requests import post,put,get,delete
from json import loads
from time import time
import csv
from math import ceil

auth = {'hash','token','other'}
base = ''

def call(method,endpoint,data=None,domain='api',body=True,status=False,header=False):
    if domain == 'api':
        base = 'https://api.bigcommerce.com/stores/'
        headers = {
            'Accept':'application/json',
            'X-Auth-Token':auth['token'],
            'Content-Type':'application/json'
        }
    elif domain == 'payments':
        base = 'https://payments.bigcommerce.com/stores/'
        headers = {
            'Authorization':auth['other'],
            'X-Auth-Token':auth['token'],
            'Content-type':'application/json',
            'Accept':'application/vnd.bc.v1+json'
        }
    if method == 'post':
        response = post(base+auth['hash']+endpoint,json=data,headers=headers)
        if status:
            print(f'Status: {response.status_code}')
        if header:
            print(f'Headers: {response.headers}')
        if body: 
            try:
                return loads(response.text)
            except:
                print("-- Raw data --")
                return response.text
        
    elif method == 'put':
        response = put(base+auth['hash']+endpoint, json=data, headers=headers)
        if status:
            print(f'Status: {response.status_code}')
        if header:
            print(f'Headers: {response.headers}')
        if body: 
            try:
                return loads(response.text)
            except:
                print("-- Raw data --")
                return response.text
        
    elif method == 'delete':
        if not data:
            response = delete(base+auth['hash']+endpoint,headers=headers)         
        if data:
            url = '?id:in='
            for item in data:
                url+=str(item)+','
            result = endpoint+url
            target = result[0:-1]
            response = delete(base+auth['hash']+target,headers=headers)
        if status:
            print(f'Status: {response.status_code}')
        if header:
            print(f'Headers: {response.headers}')
        if response.status_code == 204:
            return f'Object(s) have been deleted'
        else:
            try:
                return loads(response.text)
            except:
                print("-- Raw data --")
                return response.text
            
    elif method == 'get':
        if data:
            endpoint += '?'
            endpoint += data
        response = get(base+auth['hash']+endpoint,params=data,headers=headers)
        if status:
            print(f'Status: {response.status_code}')
        if header:
            print(f'Headers: {response.headers}')
        if body: 
            try:
                return loads(response.text)
            except:
                print("-- Raw data --")
                return response.text




class Product:
    def create(**args):
        response = call('post','/v3/catalog/products',args)
        return response

    def createv2(**args):
        response = call('post','/v2/products',args)
        return response


    def update(id,**args):
        response = call('put','/v3/catalog/products/'+str(id),args)
        return response


    def bulk_update(data):
        response = call('put','/v3/catalog/products',data)
        return response


    def retrieve(id):
        response = call('get','/v3/catalog/products/'+str(id))
        return response


    def list(query=None):
        response = call('get','/v3/catalog/products',query)
        return response


    def delete(id):
        response = call('delete','/v3/catalog/products/'+str(id))
        return response


    def bulk_delete(*args):
        response = call('delete','/v3/catalog/products',args)
        return response

    def get_prices(**args):
        response = call('post','/v3/pricing/products',args)
        return response




    class Variant:
        def create_option(product_id,**args):
            response = call('post','/v3/catalog/products/'+str(product_id)+'/options',args)
            return response


        def update_option(product_id,option_id,**args):
            response = call('put','/v3/catalog/products/'+str(product_id)+'/options/'+str(option_id),args)
            return response


        def retrieve_option(product_id,option_id):
            response = call('get','/v3/catalog/products/'+str(product_id)+'/options/'+str(option_id))
            return response


        def list_options(product_id,query=None):
            response = call('get','/v3/catalog/products/'+str(product_id)+'/options',query)
            return response


        def delete_option(product_id,option_id):
            response = call('delete','/v3/catalog/products/'+str(product_id)+'/options/'+str(option_id))
            return response

        
        def create_value(product_id,option_id,**args):
            response = call('post','/v3/catalog/products/'+str(product_id)+'/options/'+str(option_id)+'/values',args)
            return response


        def update_value(product_id,option_id,value_id,**args):
            response = call('put','/v3/catalog/products/'+str(product_id)+'/options/'+str(option_id)+'/values/'+str(value_id),args)
            return response


        def retrieve_value(product_id,option_id,value_id):
            response = call('get','/v3/catalog/products/'+str(product_id)+'/options/'+str(option_id)+'/values/'+str(value_id))
            return response


        def list_values(product_id,option_id,query=None):
            response = call('get','/v3/catalog/products/'+str(product_id)+'/options/'+str(option_id)+'/values',query)
            return response


        def delete_value(product_id,option_id,value_id):
            response = call('delete','/v3/catalog/products/'+str(product_id)+'/options/'+str(option_id)+'/values/'+str(value_id))
            return response
        
        
        def create(product_id,**args):
            response = call('post','/v3/catalog/products/'+str(product_id)+'/variants',args)
            return response


        def update(product_id,variant_id,**args):
            response = call('put','/v3/catalog/products/'+str(product_id)+'/variants/'+str(variant_id),args)
            return response


        def retrieve(product_id,variant_id):
            response = call('get','/v3/catalog/products/'+str(product_id)+'/variants/'+str(variant_id))
            return response


        def list(product_id,query=None):
            response = call('get','/v3/catalog/products/'+str(product_id)+'/variants',query)
            return response


        def delete(product_id,variant_id):
            response = call('delete','/v3/catalog/products/'+str(product_id)+'/variants/'+str(variant_id))
            return response



class Category:
    def create(**args):
        response = call('post','/v3/catalog/categories',args)
        return response


    def update(id,**args):
        response = call('put','/v3/catalog/categories/'+str(id),args)
        return response


    def retrieve(id):
        response = call('get','/v3/catalog/categories/'+str(id))
        return response


    def list(query=None):
        response = call('get','/v3/catalog/categories',query)
        return response


    def delete(id):
        response = call('delete','/v3/catalog/categories/'+str(id))
        return response


    def bulk_delete(*args):
        response = call('delete','/v3/catalog/categories',args)
        return response



class Customers:
    def create(data):
        response = call('post','/v3/customers',data)
        return response


    def update(data):
        response = call('put','/v3/customers',data)
        return response


    def list(query=None):
        response = call('get','/v3/customers',query)
        return response


    def delete(*args):
        response = call('delete','/v3/customers',args)
        return response


    def auth(**args):
        response = call('post','/v3/customers/validate-credentials',args)
        return response


    def get_payment_methods(customer_id):
        response = call('get','/v3/customers/'+str(customer_id)+'/stored-instruments')
        return response

    
    class Group: # CURRENTLY /V2
        def create(**args):
            response = call('post','/v2/customer_groups',args)
            return response


        def update(id, **args):
            data = {'id':id,'args':args}
            response = call('put','/v2/customer_groups/',data)
            return response


        def list(query=None):
            response = call('list','/v2/customer_groups',query)
            return response


        def delete(id):
            response = call('delete','/v2/customer_groups/',id)
            return response

    
    class Addresses:
        def create(data):
            response = call('post','/v3/customers/addresses',data)
            return response


        def update(data):
            response = call('bulk_put','/v3/customers/addresses',data)
            return response


        def list(query=None):
            response = call('list','/v3/customers/addresses',query)
            return response


        def delete(*args):
            response = call('bulk_delete','/v3/customers/addresses',args)
            return response


    class Attributes:
        def create(data):
            response = call('post','/v3/customers/attributes',data)
            return response


        def update(data):
            response = call('bulk_put','/v3/customers/attributes',data)
            return response


        def list(query=None):
            response = call('list','/v3/customers/attributes',query)
            return response


        def delete(*args):
            response = call('bulk_delete','/v3/customers/attributes',args)
            return response


        def apply(data):
            response = call('bulk_put','/v3/customers/attribute-values',data)
            return response


        def remove(*args):
            response = call('bulk_delete','/v3/customers/attribute-values',args)
            return response
            
        
        def export(query=None):
            response = call('list','/v3/customers/attribute-values',query)
            return response
            

    class Consent:
        def update(customer_id,**args):
            response = call('put','/v3/customers/'+str(customer_id)+'/consent',args)
            return response


        def retrieve(customer_id):
            response = call('put','/v3/customers/'+str(customer_id)+'/consent')
            return response



class Order:
    def create(**args):
        response = call('post','/v2/orders',args)
        return response

    def update(id,**args):
        response = call('put','/v2/orders/'+str(id),args)
        return response

    def retrieve(id):
        response = call('get','/v2/orders/'+str(id))
        return response

    def list(query=None):
        response = call('get','/v2/orders',query)
        return response

    def count():
        response = call('get','/v2/orders/count')
        return response

    def delete(id):
        response = call('delete','/v2/orders/'+str(id))
        return response

    def wipe():
        response = call('delete','/v2/orders')
        return response

    def get_product(order_id,product_id):
        response = call('get','/v2/orders/'+str(order_id)+'/products/'+str(product_id))
        return response

    def list_products(order_id,query=None):
        response = call('get','/v2/orders/'+str(order_id)+'/products',query)
        return response

    def list_messages(order_id,query=None):
        response = call('get','/v2/orders/'+str(order_id)+'/messages',query)
        return response

    def list_coupons(order_id,query=None):
        response = call('get','/v2/orders/'+str(order_id)+'/coupons',query)
        return response

    def list_taxes(order_id,query=None):
        response = call('get','/v2/orders/'+str(order_id)+'/taxes',query)
        return response

    def status(status_id):
        response = call('get','/v2/orders_statuses/'+str(status_id))
        return response

    def statuses():
        response = call('get','/v2/order_statuses')
        return response
        
    class Shipping:
        def update(order_id,shipping_id,**args):
            response = call('put','/v2/orders/'+str(order_id)+'/shipping_addresses/'+str(shipping_id),args)
            return response

        def retrieve(order_id,shipping_id):
            response = call('get','/v2/orders/'+str(order_id)+'/shipping_addresses/'+str(shipping_id))
            return response

        def list(order_id,query=None):
            response = call('get','/v2/orders/'+str(order_id)+'/shipping_addresses',query)
            return response

        def get_quote(order_id,shipping_id):
            response = call('get','/v2/orders/'+str(order_id)+'/shipping_addresses/'+str(shipping_id)+'/shipping_quotes')
            return response

    class Consignment:
        def list(order_id,query=None):
            response = call('get','/v2/orders/'+str(order_id)+'/consignments',query)
            return response

        def get_quote(order_id,consignment_id):
            response = call('get','/v2/orders/'+str(order_id)+'/consignments/shipping/'+str(consignment_id)+'/shipping_quotes')
            return response
    
    class Shipment:
        def create(order_id,**args):
            response = call('post','/v2/orders/'+str(order_id)+'/shipments',args)
            return response

        def update(order_id,shipment_id,**args):
            response = call('put','/v2/orders/'+str(order_id)+'/shipments/'+str(shipment_id),args)
            return response

        def retrieve(order_id,shipment_id):
            response = call('get','/v2/orders/'+str(order_id)+'/shipments/'+str(shipment_id))
            return response

        def list(order_id,query=None):
            response = call('get','/v2/orders/'+str(order_id)+'/shipments',query)
            return response

        def delete(order_id,shipment_id):
            response = call('delete','/v2/orders/'+str(order_id)+'/shipments/'+str(shipment_id))
            return response

        def bulk_delete(order_id,*args):
            response = call('delete','/v2/orders/'+str(order_id)+'/shipments',args)
            return response

        def count(order_id):
            response = call('get','/v2/orders/'+str(order_id)+'/shipments/count')
            return response

    class Transaction:
            def list(order_id,query=None):
                response = call('get','/v3/orders/'+str(order_id)+'/transactions')
                return response

            def capture(order_id):
                response = call('post','/v3/orders/'+str(order_id)+'/payment_actions/capture')
                return response

            def void(order_id):
                response = call('post','/v3/orders/'+str(order_id)+'/payment_actions/void')
                return response

            def quote_refund(order_id,**args):
                response = call('post','/v3/orders/'+str(order_id)+'/payment_actions/refund_quotes',args)
                return response

            def quote_refunds(**args):
                response = call('post','/v3/orders/payment_actions/refund_quotes',args)
                return response

            def create_refund(order_id,**args):
                response = call('post','/v3/orders/'+str(order_id)+'/payment_actions/refunds',args)
                return response

            def get_refund(order_id,refund_id):
                response = call('get','/v3/orders/'+str(order_id)+'/payment_actions/refunds/'+str(refund_id))
                return response

            def list_refunds(order_id,query=None):
                response = call('get','/v3/orders/'+str(order_id)+'/payment_actions/refunds',query)
                return response



class Gateway:
    def process_payment(**args):
        response = call('post','/payments',args,'payments')    
        return response
    
    def process(order_id,**args):
        token = Token.payment(order={'id':order_id})
        auth['other'] = 'PAT '+str(token['data']['id'])
        response = Gateway.process_payment(**args)
        return response

    def get_methods(order_id):
        response = call('get','/v3/payments/methods?order_id='+str(order_id))
        return response



class Cart:
    def create(**args):
        response = call('post','/v3/carts',args)    
        return response

    def update(id,**args):
        response = call('put','/v3/carts/'+str(id),args)    
        return response

    def retrieve(id):
        response = call('get','/v3/carts/'+str(id))    
        return response        

    def delete(id):
        response = call('delete','/v3/carts/'+str(id))    
        return response

    def get_abandoned(token):
        response = call('get','/v3/abandoned-carts/'+str(token))    
        return response


class Script:
    def create(**args):
        response = call('post','/v3/content/scripts',args)    
        return response

    def update(id,**args):
        response = call('put','/v3/content/scripts/'+str(id),args)    
        return response

    def retrieve(id):
        response = call('get','/v3/content/scripts/'+str(id))    
        return response        

    def list(query=None):
        response = call('get','/v3/content/scripts',query)    
        return response

    def delete(id):
        response = call('delete','/v3/content/scripts/'+str(id))    
        return response


class Hook:
    def create(**args):
        response = call('post','/v3/hooks',args)    
        return response

    def update(id,**args):
        response = call('put','/v3/hooks/'+str(id),args)    
        return response

    def retrieve(id):
        response = call('get','/v3/hooks/'+str(id))    
        return response        

    def list(query=None):
        response = call('get','/v3/hooks',query)    
        return response

    def delete(id):
        response = call('delete','/v3/hooks/'+str(id))    
        return response




class Token:
    def gql(**args):
        response = call('post','/v3/storefront/api-token',args)
        return response

    def customer(**args):
        response = call('post','/v3/storefront/api-token-customer-impersonation',args)
        return response

    def payment(**args):
        response = call('post','/v3/payments/access_tokens',args)
        return response


class Admin:
    def system_logs(query=None):
        response = call('get','/v3/store/systemlogs',query)
        return response


def gql(query,channel_id=1, cors='https://replit.com', token=None, customer_token=None, admin=False, account=None):
    endpoint = 'https://store-'+auth['hash']+'.mybigcommerce.com/graphql'
    
    if channel_id != 1:
        endpoint = 'https://store-'+auth['hash']+'-'+str(channel_id)+'.mybigcommerce.com/graphql'
        
    if not token:
        request = Token.gql(
            channel_id=channel_id,
            allowed_cors_origins=[cors],
            expires_at=int(time()+1000))
        token = request['data']['token']
    headers = {
        'Content-Type':'application/json',
        'Authorization':'Bearer ' + token,
    }
    
    if admin:
        if not token:
            headers = {
                'Content-Type':'application/json',
                'X-Auth-Token':auth['token'],
                'Accept': 'application/json',
            }   
        else:
            headers = {
                'Content-Type':'application/json',
                'X-Auth-Token':token,
                'Accept': 'application/json',
            }   
        endpoint = 'https://api.bigcommerce.com/stores/'+str(auth['hash'])+'/graphql'
    elif account:
        headers = {
            'Content-Type':'application/json',
            'X-Auth-Token':token,
        }   
        endpoint = 'https://api.bigcommerce.com/accounts/'+account+'/graphql'
        
    elif token and customer_token:
        headers = {
            'Content-Type':'application/json',
            'Authorization':'Bearer ' + token,
            'x-bc-customer-id': str(customer_token)
        }        
    print(endpoint)
    response = post(endpoint,json=query, headers=headers)
    try:
        return loads(response.text)
    except:
        print("-- Raw data --")
        return response.text


def v2_check(pages, configurable_fields_check=False):
    content=[]
    x = 0
    print('Scanning for Option Sets...')
    for i in range(pages):
        list = Product.list('limit=250&page='+str(i+1))
        for product in list['data']:
            try: 
                int(product['option_set_id'])
                x+=1
                print(str(product['id']) +' - ' + str(product['name']) + ' - ' + str(product['option_set_id']))
                content.append([product['id'],product['name']])
            except:
                continue
    print('Done, found '+str(x)+' Option Sets')
    with open('Product-list.csv','w',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Product ID','Product Name'])
        writer.writerows(content)
    if configurable_fields_check:
        content2 = []
        x = 0
        print('Scanning for Configurable Fields...')
        for i in range(pages):
            print('Scanning page '+str(i+1)+'...')
            list = Product.list('limit=250&page='+str(i+1))
            for product in list['data']:
                headers = {
                    'Accept':'application/json',
                    'X-Auth-Token':auth['token']
                }
                response = get('https://api.bigcommerce.com/stores/'+auth['hash']+'/v2/products/'+str(product['id'])+'/configurablefields',headers=headers)
                try:
                    loads(response.text)
                    x+=1
                    content.append([product['id'],product['name']])
                    print(str(product['id']) +' - ' + str(product['name']))
                except:
                    continue
        sheet('configurable_fields',['Product ID','Product Name'],content2)
        print('Done, found '+str(x)+' Configurable Fields')


def link_check(
    links,
    categories=True,
    brands=True,
    webpages=True,
    redirects=True,
    products=False
):
    content={
        'categories':[],
        'brands':[],
        'webpages':[],
        'redirects':[],
        'products':[]
    }
    if categories:
        print('### Checking Categories ###')
        count = call('get','/v3/catalog/trees/categories')
        cat_pages = count['meta']['pagination']['total_pages']
        print(f'-Running {str(cat_pages)} pages:')
        for i in range(cat_pages):
            print(str(i+1)+' - ',end='')
            cat_list = call('get','/v3/catalog/trees/categories?page='+str(i+1))
            for cat in cat_list['data']:
                try:
                    if cat['url']['path'] in links:
                        content['categories'].append([cat['category_id'],cat['name'],cat['url']['path']])
                except:
                    continue
    print()
    if brands:
        print('### Checking Brands ###')
        count = call('get','/v3/catalog/brands')
        brd_pages = count['meta']['pagination']['total_pages']
        print(f'-Running {str(brd_pages)} pages:')
        for i in range(brd_pages):
            print(str(i+1)+' - ',end='')
            brd_list = call('get','/v3/catalog/brands?page='+str(i+1))
            for brd in brd_list['data']:
                if brd['custom_url']['url'] in links:
                    content['brands'].append([brd['id'],brd['name'],brd['custom_url']['url']])
    print()
    if webpages:
        print('### Checking Webpages ###')
        count = call('get','/v3/content/pages?limit=250')
        page_pages = count['meta']['pagination']['total_pages']
        print(f'-Running {str(page_pages)} pages:')
        for i in range(page_pages):
            print(str(i+1)+' - ',end='')
            page_list = call('get','/v3/content/pages?limit=250&page='+str(i+1))
            for page in page_list['data']:
                if page['id'] == 79:
                    print('page 79')
                try:   
                    if page['url'] in links:
                        content['webpages'].append([page['id'],page['name'],page['url']])
                except:
                    continue
    print()
    if redirects:
        print('### Checking Redirects ###')
        count = call('get','/v3/storefront/redirects?limit=250')
        rdr_pages = count['meta']['pagination']['total_pages']
        print(f'-Running {str(rdr_pages)} pages:')
        for i in range(rdr_pages):
            print(str(i+1)+' - ',end='')
            rdr_list = call('get','/v3/storefront/redirects?page='+str(i+1))
            for rdr in rdr_list['data']:
                if rdr['to']['type'] == 'url':
                    if rdr['to']['url'] in links:
                        content['redirects'].append([rdr['id'],rdr['from_path'],rdr['to']['url']])
    print()
    if products:
        print('### Checking Products ###')
        count = call('get','/v3/catalog/products')
        prod_pages = count['meta']['pagination']['total_pages']
        print(f'-Running {str(prod_pages)} pages:')
        for i in range(prod_pages):
            print(str(i+1)+' - ',end='')
            prod_list = call('get','/v3/catalog/products?limit=250&page='+str(i+1))
            for prod in prod_list['data']:
                if prod['custom_url']['url'] in links:
                    content['products'].append([prod['id'],prod['name'],prod['custom_url']['url']])
    print()
    return content


def get_required_states():
    list = []
    countries = call('get','/v2/countries?limit=250')
    for country in countries:
        try:
            states = call('get','/v2/countries/'+str(country['id'])+'/states')
            if states[0]:
                list.append(country['country'])
        except:
            continue
    return list

def get_dup_filters():
    filter_names = []
    duplicates = []
    list = call('get','/v3/settings/search/filters/available')
    for filter in list['data']:
        if filter['name'] in filter_names:
            duplicates.append(filter)
        else:
            filter_names.append(filter['name'])

    return duplicates
    
    
def search_custom_fields(list):
    probe = Product.list('limit=1')
    pages = int(ceil(probe['meta']['pagination']['total_pages']/250))
    result = []

    for i in range(pages):
        print(f'Scanning page {str(i+1)} out of {str(pages)}')
        products = Product.list('limit=250&include=custom_fields&page='+str(i+1))
        for product in products['data']:
            if product['custom_fields']:
                fields = call('get','/v3/catalog/products/'+str(product['id'])+'/custom-fields?limit=250')
                if fields['meta']['pagination']['total_pages']>1:
                    result.append(str(product['id'])+'?')
                    print(str(product['id']) + ' has too many custom fields')
                for field in fields['data']:
                    if field['name'] in list:
                        result.append(product['id'])
                        print(product['id'])
    return result
                        

def search_options(list):
    probe = Product.list('limit=1')
    pages = int(ceil(probe['meta']['pagination']['total_pages']/10))
    result = []

    for i in range(pages):
        print(f'Scanning page {str(i+1)} out of {str(pages)}')
        products = Product.list('limit=250&include=options&page='+str(i+1))
        for product in products['data']:
            if product['options']:
                options = call('get','/v3/catalog/products/'+str(product['id'])+'/options?limit=250')
                if options['meta']['pagination']['total_pages']>1:
                    result.append(str(product['id'])+'?')
                    print(str(product['id']) + ' has too many options')
                for option in options['data']:
                    if option['name'] in list:
                        result.append(product['id'])
                        print(product['id'])        
    return result