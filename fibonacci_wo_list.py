#fibonacci without using list

a=0
b=1
n=int(input("please give the maximum number for  fibonacci sequence to be generated:"))
c=0
counter=2
print(a)
print(b)
while b<n:
#while counter<n:
    c=b
    b=a+b
    a=c
    if(b<n):
    
        print(b)
        counter+=1



def fibLessThanN(n):
    a = 0
    b = 1
    c = 0
    while(b<n):
        c = b
        b = a+b
        a = c
        print(b)

def nFibNums(n):
    a = 0
    b = 1
    c = 0
    counter = 0
    while(counter < n):
        