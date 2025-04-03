# BigCommerce-Library
Python library for BigCommerce APIs and useful utilities

# DOCUMENTATION


## Authentication

```
auth = {  
    'hash': {{STORE_HASH}},  
    'token': {{API_ACCESS_TOKEN}}  
}
```

## Formatting

Integers and strings are accepted for object IDs.  
```
(args) = (name='test', price=50)  
(array) = ([{object},{object},...])  
(query) = ('id:in=x,y,z&name:in=x,y,z')  
```

## Custom API Calls

For any call not documented below, you may use the `call()` method:
```
call(method,endpoint,body,domain='api',status=False,header=False)
```
-The `domain` parameter will switch between _api.bigcommerce_ and _payments.bigcommerce_ paths.  
-The `status` parameter will return the response status code.  
-The `header` parameter will return the response headers.

Examples:
```
call('get','/v2/orders?id:in=150')
```
```
call('put','/v3/catalog/products/id',{args})
```
```
call('post','payments',{args},'payments')
```

## Products

```
Product.   
    create(args)   
    update(id,args)   
    bulk_update(array)  
    retrieve(id)  
    list(query)
    delete(id)
    bulk_delete(id1,id2...)
    get_prices(channel_id,currency_code,customer_group_id,items[])
```
```
Product.Variant.
    create_option(product_id,args)
    update_option(product_id,option_id,args)
    retrieve_option(product_id,option_id)
    list_options(product_id,query)
    delete_option(product_id,option_id)
```
```
Product.Variant.
    create_value(product_id,option_id,args)
    update_value(product_id,option_id,value_id)
    retrieve_value(product_id,option_id,value_id)
    list_values(product_id,option_id,query)
    delete_value(product_id,option_id,value_id)
```
```
Product.Variant.
    create(product_id,args)
    update(product_id,variant_id,args)
    retrieve(product_id,variant_id)
    list(product_id,query)
    delete(product_id,variant_id)
```

## Categories

```
Category.
    create(args)
    update(id,args)
    retrieve(id)
    list(query)
    delete(id)
    bulk_delete(id1,id2...)
```

## Customers

```
Customers.
    create(array)
    update(array)
    list(query)
    delete(id1,id2...)
    auth(args)
    get_payment_methods(customer_id)
```
```
Customers.Group.
    create(args)
    update(id,args)
    list(query)
    delete(id)
```
```
Customers.Addresses.
    create(array)
    update(array)
    list(query)
    delete(id1,id2...)
```
```
Customers.Attributes.
    create(array{name,type})
    update(array{id,name})
    list(query)
    delete(id1,id2...)
    apply(array{attribute_id,customer_id,value})
    remove(id1,id2...)
    export(query)
```
```
Customers.Consent.
    update(customer_id,allow[],deny[])
    retrieve(customer_id)
```

## Orders    

```
Order.
    create(args)
    update(id,args)get
    retrieve(id)
    list(query)
    count()
    delete(id)
    wipe()
    get_product(order_id,product_id)
    list_products(order_id,query)
    status(status_id)
    statuses()
```
```
Order.
    list_messages(order_id,query)
    list_coupons(order_id,query)
    list_taxes(order_id,query)
```
```
Order.Shipping.
    update(order_id,shipping_id,args)
    retrieve(order_id,shipping_id)
    list(order_id,query)
    get_quote(order_id,shipping_id)
```
```
Order.Consignment.
    list(order_id,query)
    get_quote(order_id,consignment_id)\
```
```
Order.Shipment.
    create(order_id,args)
    update(order_id,shipment_id,args)
    retrieve(order_id,shipment_id)
    list(order_id,query)
    delete(order_id,shipment_id)
    bulk_delete(order_id,id1,id2...)
    count(order_id)
```
```
Order.Transaction.
    list(order_id,query)
    capture(order_id)
    void(order_id)
    quote_refund(order_id,args)
    quote_refunds(args)
    create_refund(order_id,args)
    get_refund(order_id,refund_id)
    list_refunds(order_id,query)
```

## Gateways

```
Gateway.
    process(order_id,args)
    process_payment(args)
    get_methods(order_id)
```

## Management

```
Cart.
    create(args)
    update(id,args)
    retrieve(id)
    delete(id)
    get_abandoned(token)
```
```
Script.
    create(args)
    update(id,args)
    retrieve(id)
    list(query)
    delete(id)
```
```
Hook.
    create(args)
    update(id,args)
    retrieve(id)
    list(query)
    delete(id)
```

## Tokens

```
Token.
    gql(channel_id,expires_at)
    customer(channel_id,expires_at)
    payment(order[id])
```

## Admin

```
Admin.
    system_logs(query)
```

## GraphQL

```
gql(query,channel_id,cors,token,customer_token,admin,account)
```

## Tools

Checking Products with Option Sets / Configurable Fields  
```
v2_check(pages,configurable_fields_check)
```

Checking used store links
```
link_check([links],categories,brands,webpages,redirects,products=false)
```

Export to CSV
```
sheet(name,headers,content)
```

Checking countries with required states
```
get_required_states()
```

