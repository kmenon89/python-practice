#get guestlist , input list, print the guest list
import csv
filename="guestlist.csv"
read="r"
write="w"
accessmode="r+"
#input guest name from user

guestname=[]
guestage=[]
name=""
age=int(10000)

while name.upper() != "DONE":
    name=input("pleases enter name of the guest(once completed enter name of the the guest as DONE):")
    age=int(input("enter the age of the guest(give 0 incase list is completed):"))
    if name.upper() != "DONE":
        guestname.append(name)
        guestage.append(age)

print(guestname)
print(guestage)

#with open(filename,accessmode) as myfile:
#myfile=open(filename,accessmode)
print("filename:", filename)
for idx,currentname in enumerate(guestname):
    with open(filename,"a") as myfile:
        print("wrote:", myfile.write(currentname + ", " + str(guestage[idx])+ "\n"))

# with open(filename,"r") as myfile:
#     content = csv.reader(myfile)
#     print("content:", content)]