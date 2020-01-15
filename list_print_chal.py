#append meal menus
#avoid menu's with Spam
#print contents separatly

menu=[]

menu.append(["e","f","g"])
menu.append(["e","g","h"])
menu.append(["g","h","i"])
menu.append(["e","h","i"])
menu.append(["g","e"])
menu.append(["g","e","g"])
menu.append(["e","h"])

for i in menu:
    if not "g" in i:
        for each in i:
            print(each)