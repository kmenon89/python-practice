#create a file with names and ages as csv file

filename="empdetails.txt"
accessmode="r+"

#open file and create file and input the data

myfile=open(filename,accessmode)
myfile.write("km,28")
myfile.write("\nkbn,28")
myfile.write("\nsm,38")

myfile.close()
#read contents of the file

myfile=open(filename,accessmode)
filecontents=myfile.read()
print(filecontents)
myfile.close()