#flames game

#variables
n1=[]
n2=[]
count=0
STRING_DIC={"F":"Friends",
            "L":"Love",
            "A":"Anger",
            "M":"Marriage",
            "E":"Enemy",
            "S":"Sister"}
STRING=["F","L","A","M","E","S"]
a=0
result=""
#user input
name1=input("please give first name:")
name2=input("please give name of the flame:")
flg=0

#convert the strings to list 

for i in name1:
    n1.append(i)
print(n1)
for i in name2:
    n2.append(i)
print(n2)

#remove the leters not common in both names
for l in n1:
    x=range(len(n1))
    if  x!=0 and flg=1:
        x=x-1
    else:
        x
    print(len(n1),x,n1)
    flg=0
    if n1[x] in n2:
        print(x,n1[x])
        n2.remove(n1[x])
        n1.remove(n1[x])
        flg=1
        print(n1,n2,x)
  

#combine the remaining letters and get the count of letters
final=n1+n2
print(final)
for x in final:
    count+=1
print(count)