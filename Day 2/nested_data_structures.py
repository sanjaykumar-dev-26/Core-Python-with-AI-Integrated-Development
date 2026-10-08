import pprint
products = {} #dict of list
products['id']=[101,102,103,104]
products['name']=['Laptop','Mouse','Keyboard','Monitor']
products['price']=[1000,50,80,300]

pprint.pprint(products)
print('\n')

products=[] #list of dicts
products.append({'id':101,'name':'Laptop','price':1000})
products.append({'id':102,'name':'Mouse','price':50})
products.append({'id':103,'name':'Keyboard','price':80})
products.append({'id':104,'name':'Monitor','price':300})

pprint.pprint(products)
print('\n')


products={} #dict of dicts
products['id']={'id1':101,'id2':102,'id3':103,'id4':104}
products['name']={'name1':'Laptop','name2':'Mouse','name3':'Keyboard','name4':'Monitor'}
products['price']={'price1':1000,'price2':50,'price3':80,'price4':300}

pprint.pprint(products)
