#experimenting with ranges

mylist=range(0,10)
print(mylist)
 
for i in mylist:
    print(i)
    list1=mylist[::7]
print(list1)
print(mylist)
for i in list1:
    print(i)
print('*'*20)
even=range(0,10,2)
for i in even:
    print(i)
even_1=mylist[::2]
print('*'*20)
for i in even_1:
    print(i)

print(even==even_1)