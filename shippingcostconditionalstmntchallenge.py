#get total value of purchase from customer calculate shipping cost

#get input from the user
total_bill=float(input("please enter the total bill amount:"))

if total_bill <50 :
    final_amnt=total_bill+10
    print("your final amount including shipping charges is $%.2f :" %final_amnt)
else:
    print("your final amount is $%.2f, your shipping is free!!" %total_bill)

