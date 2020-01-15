#iterator challenge

my_list=["a","b","c","d","e"]

My_iterator=iter(my_list)

for i in range(0,len(my_list)):
    next_item=next(My_iterator)
    print(next_item)

#similar to 
my_list=["f","g","h","i","j"]

for i in my_list:
    print(i)