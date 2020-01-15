#fibinacci series 

a=0
b=1
#n=int(input("please give the number of fibonacci sequence to be generated:"))
n=int(input("please give the maximum number for  fibonacci sequence to be generated:"))
series=[]
series.append(a)
series.append(b)
length=len(series)-1
print(length,series[length])

while len(series)<n:#--> comment when print fibonacci for a number lesser than  equal to given number
#while series[length]<=n: #-->uncomment when  print fibonacci for a number lesser than  equal to given number

    x=len(series)
    print(x)
    n1=series[x-1]+series[x-2]
    #if n1<=n : #--> uncomment when print fibonacci for a number lesser than  equal to given number
    if len(series)<n:#--> comment when print fibonacci for a number lesser than  equal to given number
        series.append(n1)
        print(series)
        length=len(series)-1
    else:
        break
    
print(series)
    
    

