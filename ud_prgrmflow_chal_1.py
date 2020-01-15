#program to get age and name and check if they are eligible to go for a 18-30 holiday

#get input from user

name=input("please enter the name:")
age=int(input("please enter your age:"))

if age:
    if 17<age<31:
        print("Hi {0} ,welcome to the 18-30 holidays".format(name))
    else:
        print("oops! you are not eligible for this trip!" )
else:
    print("Please enter a valid age!")

