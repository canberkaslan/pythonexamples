import json
data = {} #Dictionary
data['people'] = []
data ['people'].append({
    'name':'Scott',
    'website':'Stackabuse.com',
    'from':'Nebraska'
})
data ['people'].append({
    'name':'Larry',
    'website':'google.com',
    'from':'Michigan'
})
data ['people'].append({
    'name':'Tim',
    'website':'apple.com',
    'from':'Alabama'
})

#Writing
#with open('data.json','w') as xFile:
#    json.dump(data,xFile)

#Reading
with open('data.json','r') as xFile:
    data = json.load(xFile)
    for x in data['people']:
        print('Name : ' + x['name'])
        print('Website :' + x['website'])
        print('Frım : ' + x['from'])
        print('')