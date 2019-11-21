'''
sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

plakalar = {'Kocaeli':41,'Istanbul':34}

print(plakalar['Kocaeli'])
print(plakalar.values())
print(plakalar.keys())
'''
users = {
    'canberkaslan':{
        'first_name':'Canberk',
        'last_name' : 'Aslan',
        'age':31,
        'roles': ['user','writer'],
        'email': 'canberkaslan@n11.com',
        'phone' :'05372680609'
    },
    'hebehobe':{
        'first_name':'hebe',
        'last_name' : 'hove',
        'age': 24,
        'roles': ['user'],
        'email': 'hebehobe@n11.com',
        'phone' :'0121272680609'
    }
} 

print(users['canberkaslan']['roles'])