#get date and format it to dd/mm/yyyy format

import datetime
#create function

def date_function(dates):
    date_formatted=datetime.datetime.strptime(dates,"%d/%m/%Y")
    return date_formatted

#call the function

dates=input("give date:")
date_formatted=date_function(dates)
print(date_formatted)