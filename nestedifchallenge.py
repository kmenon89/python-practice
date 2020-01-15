#program to find total amount+tax 
#input country,province,total purchase amount  from the user

country=input("please give the country of purchase:").upper()
#only if country input was canada as for province ( alternative way)
# no need to diclare provice is valid variable
#if canada and the conditions outside if print the amount
#if country=="CANADA": 
province=input("please give theprovince name(applicable only if country is canada else answer NA):").upper()
bill_amount=float(input("please provide the bill amount:"))

#define tax amounts in a variable for reuse and in case of any changes
GST=0.05
PST=0.06
HST=0.13


#for capturing invalid province names
#how do i check for null strings??--> == None

provinceisvalid=False

if province!="NA" :
    provinceisvalid=True


#calculate the tax based on province,country
#any country other than canada no tax
# canada and alberta -.05% GST
#canada and ontario or new brunswick or nova scotia -0.13% HST
#canada and any other province -0.06%PST+0.05% GST

if country=="CANADA" :
    if  provinceisvalid:
        if province=="ALBERTA":
            total_bill=bill_amount+(bill_amount*GST)
            print("your total bill is {0:.2f} and {1:.2f}% of GST is applied".format(total_bill,GST))
        elif province=="ONTARIO" or province=="NEW BRUNSWICK" or province=="NOVA SCOTIA":
            total_bill=bill_amount+(bill_amount*HST)
            print("your total bill is {0:.2f} and {1:.2f}% of HST is applied".format(total_bill,HST))
        else :
            total_bill=bill_amount+(bill_amount*GST)+(bill_amount*PST)
            print("your total bill is {0:.2f} and {1:.2f}% of GST and {2:.2f}%PST  is applied".format(total_bill,GST,PST))
    else :
        print("please enter valid province name!!")
else :
    print("total bill amount is %.2f , no tax on non canadian countries"%bill_amount)