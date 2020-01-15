#program to get ip address as input , count number of segments in it and length of each segments

#get ip adress from user

ip_address=input("please enter the ip address:")
len_ip=len(ip_address)
segment=0
segment_length=""
#count the number of segments
if ip_address: 
    
    for i in range(0,len_ip):
        if (ip_address[i] == ".")  :
            segment +=1
            segment_length=len(segment_length)
            print("segment {0} length is {1}".format(segment,segment_length))
            segment_length=""
        else :
            
            segment_length =segment_length+ip_address[i]
            #print(ip_address[i],i,len_ip-1,segment_length)
            if (i==(len_ip-1)):
                segment +=1
                segment_length=len(segment_length)
                print("segment {0} length is {1}".format(segment,segment_length))
            #print(segment_length)
else:
    print("please enter an ip address!")          
       
  