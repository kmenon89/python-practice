#flames game

#variables
n1=[]
n2=[]
rem_list=[]
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


#convert the strings to list 

for i in name1:
    n1.append(i)
print(n1)
for i in name2:
    n2.append(i)
print(n2)

#remove the leters not common in both names
for x in n1:
    
    if x in n2:
        n2.remove(x)
        rem_list.append(x)
        # n1.remove(x)
for x in rem_list:
    if x in n1:
        n1.remove(x)
#combine the remaining letters and get the count of letters
final=n1+n2
print(final)
for x in final:
    count+=1
print(count)


#using letters FLAMES to find letter

    
for x in range(len(STRING)) :
        
    while a<count and len(STRING)>1:
        # print("second while a {} x {}:".format(a,x))
        # print("string({}) is {}".format(x,STRING[x]))
        if count-1==a:
                
            STRING.remove(STRING[x])
            a=-1
            x=x-1
            # print(x,STRING)
        if x==len(STRING)-1:
            x=0
        else :
            x+=1
        a+=1
result="".join(STRING)
print("the result is {}".format(STRING_DIC[result]))

