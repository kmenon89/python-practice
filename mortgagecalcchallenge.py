#mortgage calculator program
#user enters the loan amount interest rate and number of payments and program gives monthly payments

#get the inputs from the users
loanamount=float(input("enter the loan amount:"))
intrate=float(input("enter the interest rate offered:"))
noofpaymnts=int(input("enter the number of payments planned to make:"))

#calculate the monthly payment using formula


monthlypaymnt=(loanamount*(intrate*(1+intrate)*noofpaymnts))/(((1+intrate)*noofpaymnts)-1)


print("mortgage to be paid for loan amount of {0:f} for interest rate of {1:f} for {2:d} is {3:f} ".format(loanamount,intrate,noofpaymnts,monthlypaymnt))
