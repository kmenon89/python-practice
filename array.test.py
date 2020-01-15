number=[6,5,4,7,8,9,3,2]
number.sort()# prints sorted order but changes actual array too
print(number)
numbers=[6,5,4,7,8,9,3,2]
print(sorted(numbers))# doesnot change actual variable 
print(numbers)

#declaration or assignment

#use of range
sevens=range(7,1000000,7)
x=int(input("number less than 1 million"))
if x in sevens:
    print ("divisible by 7")

