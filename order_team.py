#input the scores of each team member (3 in total)
#find if they can be ranked according to scores

#declaration
A=[]
B=[]
C=[]
d=[]

#input the scores
def input_scores(nth):
    X=[]
    count=0
    n=nth
    while count<3:
        a=int(input("give score's for the {0:d}st person:".format(n)))
        X.append(a)
        count+=1
    return(X)


A=input_scores(1)
B=input_scores(2)
C=input_scores(3)

def check_if_eq():
    for x in range (len(A)):
        if A[x]==B[x]:
            continue
        elif A[x]==C[x]:
            continue
        elif B[x]==C[x]:
            continue
        else:
            return(1)

def ranking():
    count=0
    val=[]
    for x in list1:
        #print(x)
        count=0
        for y in x:
            #print(y)
            count+=y
        val.append(count)
    
    q = 0
    print(val)
    if val[0] < val[3]:
        q=check_scores(B,A)
        if q!=0:
            print("A<B")
    if  q==0:
        q=check_scores(A,B)
        if q!=0:
            print("A>B")
    q = 0
    
    if val[1] < val[4]:
        q=check_scores(C,A)
        print("inside A<C")
        if q!=0:
            print("A<C")
    if  q == 0:
        print("inside A>C")
        q=check_scores(A,C)
        print(q)
        if q!=0:
            print("A>C")
    q=0
    if val[2] < val[5]:
        q=check_scores(C,B)
        print("inside B<C")
        if q!=0:
            print("B<C")
    if q==0:
        q=check_scores(B,C)
        if q!=0:
            print("B>C")
    
    

def check_if_greater(h,g):
    p=[]
    #print(h,g)
    for x in range(len(A)):
        if h[x]>g[x]:
            p.append(1)
        else:
            p.append(0)
    return(p)

def check_scores(h,g):
    l=0
    m=0
    k = -1 
    for x in range(len(A)):
        l=+h[x]
        m=+g[x]
        if h[x]>g[x]:
            continue
        elif l>m:
            k=1
        else :
            k=0
    return(k)
    
    

        
def check_if_lessthan(h,g):
    p=[]
    #print(h,g)
    for x in range(len(A)):
        if h[x]<g[x]:
            p.append(1)
            #print(p)
        else:
            p.append(0)
    return(p)
    


j= check_if_eq()
if j==1:
    d=check_if_greater(A,B)
    #print(d)
    e=check_if_greater(A,C)
    # print(e)
    f=check_if_greater(B,C)
    # print(f)

    g=check_if_lessthan(A,B)
    # print(g)
    h=check_if_lessthan(A,C)
    # print(h)
    i=check_if_lessthan(B,C)
    # print(i)
    list1=[d,e,f,g,h,i]
    print(list1)
    c=ranking()
else:
    print("Not able to rank!")

