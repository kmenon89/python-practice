#direction program
locations={0:"quit",
           1:"road",2:"building",3:"hill",4:"valley",5:"forest"}
exits=[{"Q":0},
        {"W":2,"E":3,"S":4,"N":5,"Q":0},
        {"N":5,"Q":0},
        {"W":1,"Q":0},
        {"N":1,"W":2,"Q":0},
        {"W":2,"S":1,"Q":0}]

loc=1
while True:
    available_exits=""
    print(exits[loc])#--> rints dictionary in 1st position of list
    #for i in exits[loc].keys():
        #print(i)
        #available_exits += i+","
    #all 3 lines above can be replaced using joint 
    available_exits=",".join(exits[loc].keys())
    print(locations[loc])
    if loc==0:
        break
    direction=input("available exits are " + available_exits). upper()
    print(loc)
    if direction in exits[loc]:
        loc=exits[loc][direction]
    else:
        print("you cannot go in that dir")

exits=dict(exits)