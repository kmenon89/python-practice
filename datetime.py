import time
print(time.gmtime(0))#--> prints epoch time
print(time.localtime().tm_mday)
time_here=time.localtime()
print (time_here)#--> tuple 
print("year:",time_here[0],time_here.tm_year)#-->year: 2018 2018
print("year:",time_here[1],time_here.tm_mon)#-->year: 06 06
print("year:",time_here[2],time_here.tm_mday)#-->year: 12 12


from time import time as mytime

print(mytime()) #as int of seconds

print("time:",time.get_clock_info("time"))
print("process_time:",time.get_clock_info("process_time"))
print("monotonic:",time.get_clock_info("monotonic"))
#print("Perf_counter:",time.get_clock_info("Perf_counter"))


##timezones:

print("epoch on this system starts at:"+ time.strftime("%c",time.gmtime(0)))
print("current timezone is  {0} with an offset of {1} ".format(time.tzname[0],time.timezone))
if time.daylight!=0:
    print("daylight saivng is in effect")
    print("the DST timezone is:" + time.tzname[1])