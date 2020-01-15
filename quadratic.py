#find roots of quadratic equation
#accespt A,B,C output root1,root2
import math

#function to get input from user
def get_input(nth):
    n=nth
    A=int(input("please give the {0:d} th value as real number: ".format(n)))
    #A=int(raw_input("please give the {0:d} th value as real number: ".format(n)))
    if A==0 and n==1:
        A=1
    return(A)

#function to find roots
def find_root(a,b,c):
    A=a
    B=b
    C=c
    if (B*B)<(4*A*C):
        x=0
        y=0
    else:
        x=(-B+math.sqrt(((B*B)-(4*A*C))))//(2*A)
        y=(-B-math.sqrt(((B*B)-(4*A*C))))//(2*A)
    return(x,y)

A=get_input(1)
B=get_input(2)
C=get_input(3)
#print(A,B,C)

first=find_root(A,B,C)
print(first[0])
print(first[1])

    



