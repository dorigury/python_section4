import simplejson as json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Kim',
    'website': 'naver.com',
    'from': 'Seoul',
    'grade': [95,77,89,91]
})
data['people'].append({
    'name': 'Park',
    'website': 'google.com',
    'from': 'Busan',
    'grade': [85,67,100,94]
})
data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon',
    'grade': [98,79,99,92]
})

#print(data)
#{'people': [{'website': 'naver.com', 'name': 'Kim', 'from': 'Seoul'}, {'website': 'google.com', 'name': 'Park', 'from': 'Busan'}, {'website': 'daum.net', 'name': 'Lee', 'from': 'Incheon'}]}

with open('d:/bbb/member1.json', 'w') as outfile:
    json.dump(data, outfile)

with open('d:/bbb/member1.json', 'r') as infile:
    r = json.load(infile)
    #print(type(r))
    #print(r)

    print("="*40)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        grade = ''
        for g in p['grade']:
            grade = grade + ' ' + str(g)

        print('Grade:', grade.lstrip())
        print('')
