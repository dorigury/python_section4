import simplejson as json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Kim',
    'website': 'naver.com',
    'from': 'Seoul',
})
data['people'].append({
    'name': 'Park',
    'website': 'google.com',
    'from': 'Busan'
})
data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon'
})

#print(data)
#{'people': [{'website': 'naver.com', 'name': 'Kim', 'from': 'Seoul'}, {'website': 'google.com', 'name': 'Park', 'from': 'Busan'}, {'website': 'daum.net', 'name': 'Lee', 'from': 'Incheon'}]}

e = json.dumps(data, indent=4)
#print(type(e))
#print(e)

d = json.loads(e)
#print(type(d))
#print(d)

with open('d:/bbb/member.json','w') as outfile:
    outfile.write(e)

with open('d:/bbb/member.json','r') as infile:
    r = json.loads(infile.read())
    #print("="*80)
    #print(type(r))
    #print(r)

    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
