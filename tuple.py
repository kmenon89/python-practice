#read tuple ,print details 

imelda="more mayhem","Imelda May",2011,((1,"Pulling"),
(2,"psycho"),(3,"Mayhem"),(4,"Kentish"))

print(imelda)

album,artist,year,tracks=imelda
print(album)
print(artist)
print(year)
print(tracks)
print("*"*5)
print(album,artist,year,tracks)
print("*"*5)
for i in tracks:
    track,title=i
    print("\t track  {0} is title {1}".format(track,title))

