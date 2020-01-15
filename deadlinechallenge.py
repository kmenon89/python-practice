#input deadline date, calculate how many days till completion
#print in weeks and days
#import date time class 
import datetime

#get input from user
deadline=input('give the date of deadline (dd/mm/yyyy) in given format:')
#deadline=datetime.datetime.strptime(deadline,"%d %b %Y").date() -->.date() to specify we are taking only the date part
#convert input from user to date format
deadline_time=datetime.datetime.strptime(deadline,"%d/%m/%Y")
deadline=datetime.datetime.strptime(deadline,"%d/%m/%Y").date()

print(deadline.strftime('%d/%b/%Y'))

# get the current date and calculate days until deadline
curdate=datetime.date.today()
curtime=datetime.datetime.now() #gives time as well
daysleft=deadline-curdate
timeleft=deadline_time-curtime

# to find number of weeks and days
numbofweeks=daysleft.days / 7 #pick only date part from days delta
numbofdayslft=daysleft.days%7

print("only {0:d} days left to your sumbission date".format(daysleft.days))
print(timeleft)
print("only %d weeks" %numbofweeks +" and %d days left for completion" %numbofdayslft)

# datetime gives time part
#print(curdate.strftime('%d/%b/%Y %H:%M:%S')) --> full format of date
# input should be same as how we convert in strptime but print can be modified
#deadline=input('give the date of deadline (dd mon yyyy) in given format')
#deadline=datetime.datetime.strptime(deadline,"%d %B %Y").date()
#print(deadline.strftime('%b/%d/%Y'))