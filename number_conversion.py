#convert number to binary or octa or hex

user_ip=int(input("please enter a number in decimal:"))
convert_to=int(input("please input the system to be converted"
           "to(2,8,16) :"))

# variable delarations
number_con=[]
print(number_con)
k=0
number_final=''
#to convert decimal to req format divide by number take modulus
while user_ip!=1 :
    if user_ip==0:
        number_con.append(str(0))
        break
    print(number_con)
    k=user_ip%convert_to
    number_con.append(str(k))
    user_ip=user_ip//convert_to
    print(number_con,user_ip)
    

#when  number is 1 
else:
    
    k=1
    number_con.append(str(k))
#print(number_con)

#print the output backwards as we need to place reminders backwards
for i in range(len(number_con)-1,-1,-1):
    #print(i)
    #if i in ['0123456789']:
    number_final+=number_con[i]
    print(number_con[i])

print(number_final)