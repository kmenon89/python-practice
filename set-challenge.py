#get input text,return all letters in alphabetical order except for vowels

#get input

inp=input("please enter the string:").upper()


#initialise variables
a=set()
vowels=set(["A","E","I","O","U"])

for i in inp:
    #print(i)
    if i.isalpha():
        a.add(i)
    else :
        continue

print(a)

set_final=a.difference(vowels)
print(sorted(set_final))


