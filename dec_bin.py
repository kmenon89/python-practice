#powers of 2
#change the (2**i) to 8 to octal

power=[]
numb=0
for i in range(15,-1,-1):
    power.append(2 ** i)

print(power)

x=int(input("number to be converted:"))

printing=False

for i in power:
    #print(numb,x,i)
    numb=x//i
    #print(numb,end="*")
    if x !=0 :
        printing=True
    if printing==True:
        print(numb,end='')
    x %= i
    #print(x)
