#given n number of intergers find how many numbers needs to be removed from the series to make GCD =1 , if not possible give -1 if already GCD =1 give 0

#input
inp=[5,7,8,9,1]
#inp.sort()
#find gcd


# def gcd_cal(h,g):
#     a=g%h  
#     count=0
#     while a!=0:
#         count+=1
#         g=h
#         h=a
#         print(a,g,h)
#         a=g%h 
        
#     else :
#         a=1
#         return(a)
#         print(count)

# #call gcd cal
# l=gcd_cal(inp[0],inp[1])
# leng=len(inp)-1
# for i in range(2,leng):
#     print(l)
#     l=gcd_cal(l,inp[i])
#     print(l)

# print(l)

def find_gcd(x, y):
     
    while(y):
        x, y = y, x % y
     
    return x
         
# Driver Code        
l = [5,7,8,9,1]
 
num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)
 
for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])
     
print(gcd)