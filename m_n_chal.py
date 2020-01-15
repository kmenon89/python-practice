#input from user 2 number
#o/p sum of the number

start=int(input("give starting number:"))
end=int(input("give ending number >starting number:"))

sum=0

m=start

while m<=end:
    sum=sum+m
    m+=1
print("sum is : {}".format(sum))


