#write  a multiplication table to file
m=0

with open('multiplication.txt','a') as mult:
    for i in range(2,13,1):
        print("i {0}".format(i))
        for j in range(1,13):
            print("j {0}".format(j))
            m=j*i
            print('{1:>2} times {0} equals {2}'.format(j,i,m),file=mult)
        