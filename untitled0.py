d1 = {'id':5, 'name':'john', 'age':18, 8:['a number',100]}
#d2 = {}   # 建立空的dict資料組

print(d1['id'])
#print(d1[8])
d1[123] = 456
#print(d1)
d1['name'] = 'Amy'
#print(d1)

d1.pop('age')
#print(d1)
#print(len(d1)) #幾把鑰匙
#print('age' in d1.keys())
#print('name' in d1.keys())

d2 = {'Cherry':1224,'Dora':830}
d1.update(d2)
'''
for k in d1.keys():
    print(k)
for v in d1.values():
    print(v)
    
for k,v in d1.items():
    print(k,v)
    '''