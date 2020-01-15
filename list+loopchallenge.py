#get input from users to type guest list and print them all


#initialise list and the variables
guests=[]
name=""

#initial input from user with the end of list keyword specified
name=input("give the name of the guest( at the end of list please type Done):")

#loop until end of list 
while name.upper() != 'DONE' :
    guests.append(name)
    name=input("name of the next guest( at the end of list please type Done):")
    #print and sort the list at the end of list
    if name.upper() == 'DONE' :
        guests.sort()
        print(guests)


