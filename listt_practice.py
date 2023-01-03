T1 = {'eat':'everything','love':'upgrade_himself_everyday','learning':'Kubernetes'}
print(T1.keys())
print(T1.values())
print(T1.items())

for key in T1.keys():
    print(key)
for value in T1.values():
    print(value)

for key,value in T1.items():
    print(key,value)

T1['internet'] = 'wifi'
T1.update({'eat':'chicken'})
print(T1)
print(T1.get('love')) 



