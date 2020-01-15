#all about dictiionaries

#create
dicti={1:'a',2:'b',3:'c'}
print(dicti)
print(dicti[1])

#append
dicti[4]='d'
print(dicti)
#deletion
del dicti[4]
print(dicti)
#get a value
print(dicti.get(2))
#clear whole dicti
dicti.clear()
print(dicti)

#sort dicti
dicti={2:'a',3:'b',1:'c'}
print(dicti)
order=dicti.keys()
print(order)
order=list(dicti.keys())
print(order)
order.sort()
print(order)
print(dicti)
ordered=sorted(list(dicti))
print(ordered)
print(dicti)
print(list(dicti))


#print items of dicti

print(dicti.values())
print(dicti.keys())
print(dicti.items())

#conv
tup=tuple(dicti.items())
print(tup)
print(dict(tup))

#update,copy

print(dicti)
dict2={4:"d",5:"e",6:"f"}
print(dict2)

#print(dicti.update(dict2))--> prints none but updates the dictionary
#print(dict2.update(dicti))--> prints none but updates the dictionary




dicti.update(dict2)
print(dicti)
print(dict2)
dict3=dict2.copy()
print(dict3)
print(dict3.update(dicti))
print(dict3)
print(dict2)